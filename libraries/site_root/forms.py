from wtforms import StringField, validators, PasswordField
from wtfrecaptcha.fields import RecaptchaField
from libraries.endemic.form import MyBaseForm as Form
from libraries.regex import username
from configuration import config

username_length = int(config['app']['USERNAME_LENGTH'])
recaptcha_pub_key = config['app']['RECAPTCHA_PUB_KEY']
recaptcha_priv_key = config['app']['RECAPTCHA_PRIV_KEY']


class NewUser(Form):
    username = StringField('User Name',
                           [validators.Length(
                               min=4,
                               max=username_length),
                            validators.Regexp(
                                username,
                                message='Username ' +
                                'must be alphanumeric ' +
                                '(underscores allowed)')])
    email = StringField('Email', [validators.Email()])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    captcha = RecaptchaField(
        public_key=recaptcha_pub_key,
        private_key=recaptcha_priv_key,
        secure=False)


class Login(Form):
    loginname = StringField('Email or Username',
                            [validators.Required()])
    password = PasswordField('Password', [validators.Required()])


class PasswordReset(Form):
    loginname = StringField('Email or Username',
                            [validators.Required()])
