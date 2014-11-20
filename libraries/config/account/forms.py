from wtforms import StringField, validators, PasswordField

from libraries.endemic.form import MyBaseForm as Form


class Email(Form):
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [validators.Required()])


class Password(Form):
    current_password = PasswordField('Current Password',
                                     [validators.Required()])
    new_password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
