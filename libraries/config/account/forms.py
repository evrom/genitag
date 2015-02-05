from wtforms import StringField, validators, PasswordField
from wtfrecaptcha.fields import RecaptchaField
from libraries.endemic.form import MyBaseForm as Form
from configuration import config
recaptcha_pub_key = config['app']['RECAPTCHA_PUB_KEY']
recaptcha_priv_key = config['app']['RECAPTCHA_PRIV_KEY']


class Email(Form):
    email = StringField('Email', [validators.Email()])
    # password = PasswordField('Current Password', [validators.Required()])
    captcha = RecaptchaField(
        public_key=recaptcha_pub_key,
        private_key=recaptcha_priv_key,
        secure=False)


class Password(Form):
    current_password = PasswordField('Current Password',
                                     [validators.Required()])
    new_password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
