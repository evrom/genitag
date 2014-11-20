from itsdangerous import URLSafeSerializer
from bottle import abort
from configparser import ConfigParser
import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../config.ini')
config = ConfigParser()
config.read(filename)
secret_key = config['app']['SECRET_KEY']

salt = 'signed'

s = URLSafeSerializer(secret_key)


def sign_message(message):
    signed_message = s.dumps(message)
    return signed_message


def unsign_message(signed_message):
    try:
        return s.loads(signed_message)
    except:
        return abort(500, 'bad signature')
