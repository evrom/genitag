from wtforms import Form
from wtforms.csrf.core import CSRF
from configuration import config
from bottle import request
secret_key = config['app']['COOKIE_SECRET_KEY']
csrf_cookie_name = config['app']['CSRF_COOKIE_NAME']


class CSRFMethod(CSRF):
    def setup_form(self, form):
        self.csrf_context = form.meta.csrf_context
        return super(CSRFMethod, self).setup_form(form)

    def generate_csrf_token(self, csrf_token):
        return request.csrf_token

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
