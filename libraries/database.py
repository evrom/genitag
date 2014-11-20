from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer,\
    String, MetaData, ForeignKey, LargeBinary,\
    Boolean, DateTime, func, Float, UniqueConstraint
from configparser import ConfigParser
from datetime import datetime as timestamp
from sqlalchemy.sql import expression
import os
directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../config.ini')
config = ConfigParser()
config.read(filename)
database_uri = config['app']['SQLALCHEMY_DATABASE_URI']
username_length = int(config['app']['USERNAME_LENGTH'])

event_title_length = int(config['app']['EVENT_TITLE_LENGTH'])
task_title_length = int(config['app']['TASK_TITLE_LENGTH'])
engine = create_engine(database_uri)
metadata = MetaData()
users = Table('users', metadata,
              Column('id', String(length=username_length),
                     primary_key=True,
                     unique=True, index=True, nullable=False),
              Column('email', String(255),
                     unique=True),
              Column('info', LargeBinary,  nullable=True),
              Column('pbkdf2', LargeBinary, nullable=False),
              Column('emailverified', Boolean, default=False,
                     server_default=expression.false()))


skill_index = Table('skill_index', metadata,
                    Column('id', Integer, primary_key=True,
                           index=True),
                    Column('en', String(25)))


user_skills = Table('user_skills', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('user_id', String(username_length),
                           ForeignKey("users.id",
                                      onupdate="CASCADE",
                                      ondelete="CASCADE"),
                           index=True),
                    Column('skill_id', Integer,
                           ForeignKey("skill_index.id",
                                      onupdate="CASCADE",
                                      ondelete="CASCADE"),
                           index=True),
                    Column('description', String(255), nullable=True),
                    UniqueConstraint('user_id', 'skill_id',
                                     name='uix_user_skill'))


events = Table('events', metadata,
               Column('id', Integer, primary_key=True,
                      index=True),
               Column('user_id', String(username_length),
                      ForeignKey("users.id",
                                 onupdate="CASCADE",
                                 ondelete="CASCADE")),
               Column('title', String(length=35)),
               Column('info', String(length=350)),
               Column('location', String(length=100)),
               Column('timestamp', DateTime,
                      default=timestamp.utcnow,
                      server_default=func.now()),
               Column('event_datetime', DateTime))
"""
tasks = Table('tasks', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String(length=task_title_length)),
              Column('info', LargeBinary),
              Column('user_id', String(username_length),
                     ForeignKey("users.id",
                                onupdate="CASCADE",
                                ondelete="CASCADE"),
                     index=True),
              Column('skill_id', Integer,
                     ForeignKey("skill_index.id",
                                onupdate="CASCADE",
                                ondelete="CASCADE"),
                     index=True),
              Column('timestamp', DateTime,
                     default=timestamp.utcnow,
                     server_default=func.now()))

"""
