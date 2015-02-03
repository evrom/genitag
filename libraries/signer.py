from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from bottle import abort
from configuration import config

secret_key = config['app']['SECRET_KEY']

salt = 'signed'

s = URLSafeSerializer(secret_key)
timed_s = URLSafeTimedSerializer(secret_key)


def sign_message(message):
    signed_message = s.dumps(message)
    return signed_message


def unsign_message(signed_message):
    try:
        return s.loads(signed_message)
    except:
        return abort(500, 'bad signature')


def sign_timed_message(message):
    signed_message = timed_s.dumps(message)
    return signed_message


def unsign_timed_message(signed_message, max_age):
    try:
        return timed_s.loads(signed_message, max_age=max_age)
    except:
        return abort(500, 'bad signature')
