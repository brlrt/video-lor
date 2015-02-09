# Run this file in order to create the necessary tables
from database import *
from peewee import create_model_tables
create_model_tables([Loop])
