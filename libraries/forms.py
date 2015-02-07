from wtforms import StringField, validators,\
    TextAreaField, PasswordField, RadioField, HiddenField
from wtfrecaptcha.fields import RecaptchaField
from libraries.endemic.form import MyBaseForm as Form
from libraries.regex import username
from configuration import config

username_length = int(config['app']['USERNAME_LENGTH'])
recaptcha_pub_key = config['app']['RECAPTCHA_PUB_KEY']
recaptcha_priv_key = config['app']['RECAPTCHA_PRIV_KEY']


class Blank(Form):
    pass


class NewEvent(Form):
    date = StringField('Date',
                       [validators.DataRequired(),
                        validators.Length(min=1, max=35)])
    time = StringField('Time (local time for event)',
                       [validators.DataRequired(),
                        validators.Length(min=1, max=35)])
    location = StringField('Location',
                           [validators.DataRequired(),
                            validators.Length(min=1, max=120)])
    title = StringField('Title',
                        [validators.DataRequired(),
                         validators.Length(min=1, max=70)])
    description = TextAreaField('Give details on event',
                                [validators.Length(min=1, max=1200)])


class SendEmail(Form):
    email = StringField('Email Address',
                        [validators.Email()])
    captcha = RecaptchaField(
        public_key=recaptcha_pub_key,
        private_key=recaptcha_priv_key,
        secure=False)


class ResetPassword(Form):
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class ChangeEmail(Form):
    password = PasswordField('Password', [
        validators.Required()
    ])


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


# class PasswordReset(Form):
#    loginname = StringField('Email or Username',
#                            [validators.Required()])


class Skill(Form):
    description = TextAreaField('Describe your experience with this skill',
                                [validators.Length(min=1, max=255)])


class ChangePassword(Form):
    current_password = PasswordField('Current Password',
                                     [validators.Required()])
    new_password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class Avatar(Form):
    avatar_type = RadioField('',
                             choices=[
                                 ('gravatar', 'Use gravatar'),
                                 ('avatarsio', 'Use custom avatar')])
    avatar_url = HiddenField('', [
        validators.URL(),
        validators.Optional()])


class ContactEmail(Form):
    contactemail = StringField('Email', [validators.Email()])
    pgpmirror = StringField('Optional: PGP Mirror (URL)', [
        validators.URL(),
        validators.Optional()])
    pgpfingerprint = StringField('Optional: PGP Fingerprint (Hex)', [
        validators.Regexp(r"^[A-Fa-f0-9\s]{1,64}$",
                          message='Must be Hex (0-F) (spaces OK)'),
        validators.Length(min=1, max=64),
        validators.Optional()])


class Location(Form):
    location = StringField('Location',
                           [validators.Length(min=1, max=35)])


class Twitter(Form):
    twittername = StringField('Twitter Handle',
                              [validators.Length(
                                  min=2,
                                  max=15),
                               validators.Regexp(
                                   r"^[A-Za-z0-9_]{1,15}$",
                                   message='Username ' +
                                   'must be alphanumeric ' +
                                   '(underscores allowed)')])


class Github(Form):
    githubname = StringField('User Name',
                             [validators.Length(
                                 min=2,
                                 max=15),
                              validators.Regexp(
                                  r"^[A-Za-z0-9_]{1,15}$",
                                  message='Username '
                                  'must be alphanumeric '
                                  '(underscores allowed)')])


class Website(Form):
    websiteurl = StringField('Website URL', [
        validators.URL(),
        validators.Optional()])


class Name(Form):
    name = StringField('Name',
                       [validators.Length(min=1, max=35)])


class ImGoodAt(Form):
    description = TextAreaField('What things are you good at? '
                                'Describe your experiences and '
                                'link portfolios of your work',
                                [validators.Length(min=1, max=350)])


class ICareAbout(Form):
    description = TextAreaField('What things do you care about?',
                                [validators.Length(min=1, max=350)])


class ContactMe(Form):
    description = TextAreaField('In what situation would you like '
                                'to be contacted? How should someone '
                                'contact you?',
                                [validators.Length(min=1, max=350)])


class EventTitle(Form):
    title = StringField('Title',
                        [validators.DataRequired(),
                         validators.Length(min=1, max=70)])


class EventDateTime(Form):
    date = StringField('Date',
                       [validators.DataRequired(),
                        validators.Length(min=1, max=35)])
    time = StringField('Time (local time for event)',
                       [validators.DataRequired(),
                        validators.Length(min=1, max=35)])


class EventLocation(Form):
    location = StringField('Location',
                           [validators.DataRequired(),
                            validators.Length(min=1, max=120)])


class EventDescription(Form):
    description = TextAreaField('Give details on event',
                                [validators.Length(min=1, max=1200)])
