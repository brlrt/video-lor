from flask import Flask, render_template, request, flash
from database import *
import peewee


# ==============================================================
# LoR (Listen on Repeat), Socratic Coding Challenge            #
# Author(s): Chaoyi Zha                                        #
# To start the app, edit `config.py` and run `../runserver.py` #
# ==============================================================
app = Flask("lor")
app.secret_key = "keyboardcat/changethis"

@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")

@app.route("/watch", methods=["GET"])
def loop_video():
    video_ID = request.args['v']
    try:
        tlq = Loop.select().where(Loop.video_id == video_ID).first()
        total_loops = tlq.video_loops
    except:
        total_loops = 0 # Video never played before, default to 0

    return render_template("video.html", videoId=video_ID, globalTimesLooped=total_loops)

@app.route("/mostpopular")
def most_popular():
    # Shows most popular videos, based on loops
    i = 0
    top_ten_vids = [];

    for vid_loops in Loop.select().order_by(Loop.video_loops.desc()):
        top_ten_vids.append({"loops": vid_loops.video_loops, "id": vid_loops.video_id})
        i += 1
        if i >= 9:
            break
    return render_template("leaderboard.html", top_vids=top_ten_vids)



@app.route("/api/loopcount", methods=["GET", "POST"])
def loop_count():
    # This method increments the loop count for the specific video
    # in the database, and returns to the user the total amount of times
    # the video has been looped. (cumulative, across all users)

    video_id = request.form['videoid']

    # Enumerate an array with query contents
    fields = {"video_id": video_id, "video_loops": 1} # Default loop count to 1
    upsert_data(fields)

    # Get total loops
    tlq = Loop.select().where(Loop.video_id == fields["video_id"]).first()
    total_loops = tlq.video_loops
    return str(total_loops)

def upsert_data(fields):
    # Accepts array `fields`:
    #    video_id: String, YouTube video ID
    #    video_loops: Integer, video loop count

    exq = Loop.select().where(Loop.video_id == fields["video_id"]).exists()
    print exq
    # If video_id already exists, then increment; otherwise, insert loop amnt (1)
    if exq == False:
        # Create query object, then execute the query
        insq = peewee.InsertQuery(Loop, fields)
        insq.execute()
    else:
        # Perform an atomic update to increment loop count
        target_loop = Loop.select().where(Loop.video_id == fields["video_id"]).first()
        target_loop.video_loops += 1
        target_loop.save()

    return;
