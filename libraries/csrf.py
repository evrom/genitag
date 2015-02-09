from bottle import response, request
import functools
import base64
import os
from configuration import config
secret_key = config['app']['COOKIE_SECRET_KEY']
csrf_cookie_name = config['app']['CSRF_COOKIE_NAME']


def generate_csrf_token():
    token = base64.b64encode(os.urandom(8))
    response.set_cookie(csrf_cookie_name, token,
                        secret=secret_key,
                        path='/')
    request.csrf_token = token.decode('UTF-8')


def csrf(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        generate_csrf_token()
        # Pages with CSRF tokens should not be cached
        response.headers[str('Cache-Control')] = 'private no-cache'
        return func(*args, **kwargs)
    return wrapper
