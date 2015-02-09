LoR (socratic-challenge)
======================

Play YouTube videos on repeat.

#### Running LoR:

1 - Create a `virtualenv`, and activate the env (optional -- `virtualenv` can be installed through `pip install virtualenv`):

    $ virtualenv env && source env/bin/activate

2 - Install dependencies:

    $ pip install -r requirements.txt

3 - Edit appropriate configuration files: 

    Fill in with appropriate database/API credentials: `config.py`, `static/leaderboard.js
    
4 - Create LoR's database, then enumerate tables:

    $ python lor/createdb.py
    
5 - Run LoR:

    $ python runserver.py


LoR will run on port 5000. To change this port, edit `runserver.py`
