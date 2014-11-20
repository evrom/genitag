from itsdangerous import URLSafeTimedSerializer
from configparser import ConfigParser
import os
from datetime import datetime, timedelta, time
from bottle import request, response

directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../config.ini')
config = ConfigParser()
config.read(filename)
secret_key = config['app']['SECRET_KEY']
session_cookie_name = config['app']['SESSION_COOKIE_NAME']
session_expiration_seconds = int(config['app']['SESSION_EXPIRATION_SECONDS'])

salt = 'session'


def get_serializer():
    if not secret_key:
        return None
    return URLSafeTimedSerializer(secret_key,
                                  salt=salt)


def new_session(session_data):
    serializer = get_serializer()
    val = serializer.dumps(session_data)
    return val


def set_session(session_data):
    expires = datetime.combine(
        datetime.utcnow(), time()
    )+timedelta(seconds=session_expiration_seconds)
    value = new_session(session_data)
    return response.set_cookie(
        session_cookie_name, value, expires=expires, httponly=True)


def open_session():
    val = request.get_cookie(session_cookie_name)
    max_age = session_expiration_seconds
    serializer = get_serializer()
    session_data = serializer.loads(val, max_age=max_age)
    return session_data


def remove_session():
    response.delete_cookie(session_cookie_name)
    return
