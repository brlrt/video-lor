from flask import Flask, url_for, render_template, request, flash
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
    tlq = Loop.select().where(Loop.video_id == video_ID).first()
    total_loops = tlq.video_loops
    return render_template("videopage.html", videoId=video_ID, globalTimesLooped=total_loops)

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
