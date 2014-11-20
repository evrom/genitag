from wtforms import Form
from wtforms.csrf.core import CSRF
from configparser import ConfigParser
import os
from bottle import response, request
import base64
directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../../config.ini')
config = ConfigParser()
config.read(filename)
secret_key = config['app']['SECRET_KEY']
csrf_cookie_name = config['app']['CSRF_COOKIE_NAME']
salt = config['app']['CSRF_TOKEN_SALT']


class CSRFMethod(CSRF):
    
    def setup_form(self, form):
        self.csrf_context = form.meta.csrf_context
        return super(CSRFMethod, self).setup_form(form)

    def generate_csrf_token(self, csrf_token):
        token = base64.b64encode(os.urandom(8))
        response.set_cookie(csrf_cookie_name, token,
                            secret=secret_key,
                            path='/')
        token_unicode = token.decode('UTF-8')
        return token_unicode

    def validate_csrf_token(self, form, field):
        cookie_token = request.get_cookie(csrf_cookie_name,
                                          secret=secret_key)
        cookie_token_unicode = cookie_token.decode('UTF-8')
        if field.data != cookie_token_unicode:
            raise ValueError('Invalid CSRF')


class MyBaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = CSRFMethod
