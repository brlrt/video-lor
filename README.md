LoR (socratic-challenge)
======================

Play YouTube videos on repeat.

Spec: https://docs.google.com/document/d/1A9MWbW9qrdY6ia5e4gzcoT-S2WEnkBpDIl31J9KTiPs/edit#heading=h.8yomclhc3ktz

#### Running LoR:

1 - Create a `virtualenv`, and activate the env (optional -- `virtualenv` can be installed through `pip install virtualenv`):
    `$ virtualenv env && source env/bin/activate`
2 - Edit appropriate configuration files: 
    Fill in with appropriate database/API credentials: `config.py`, `static/leaderboard.js`
3 - Create LoR's database, then enumerate tables:
    `$ python lor/createdb.py`
4 - Run LoR:
    `$ python runserver.py`

LoR will run on port 5000. To change this port, edit `runserver.py`
