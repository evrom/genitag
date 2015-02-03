from wtforms import StringField, validators, PasswordField, HiddenField
from wtfrecaptcha.fields import RecaptchaField
from libraries.endemic.form import MyBaseForm as Form
from configuration import config

username_length = int(config['app']['USERNAME_LENGTH'])
recaptcha_pub_key = config['app']['RECAPTCHA_PUB_KEY']
recaptcha_priv_key = config['app']['RECAPTCHA_PRIV_KEY']


class Resend(Form):
    email = StringField('Email Address',
                        [validators.Email()])
    captcha = RecaptchaField(
        public_key=recaptcha_pub_key,
        private_key=recaptcha_priv_key,
        secure=False)


class Reset(Form):
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
