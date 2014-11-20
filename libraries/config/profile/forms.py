from wtforms import StringField, validators, RadioField, HiddenField
from libraries.endemic.form import MyBaseForm as Form


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
    hide = RadioField('Hide Email with Recaptcha',
                      choices=[('hide', 'hide'), ('plaintext', 'plaintext')])
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
