from libraries.mailer import send_email
from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from configuration import config
secret_key = config['app']['SECRET_KEY']
email_verify_salt = config['app']['EMAIL_VERIFY_SALT']
reset_password_salt = config['app']['RESET_PASSWORD_SALT']
change_email_salt = config['app']['CHANGE_EMAIL_SALT']


def email_verify(username, email):
    s = URLSafeSerializer(secret_key, salt=email_verify_salt)
    token = s.dumps(
        dict(
            u=username,
            e=email))
    url = 'http://www.genitag.org/action/accountverify?token=' + token
    subject = 'Verify email for Genitag account'
    message = 'visit this link to verify your email address to the account with the username ' \
              + username + '\r\n' + 'link: ' + url
    send_email(message, subject, email)
    return None


def reset_password(username, email):
    s = URLSafeTimedSerializer(secret_key, salt=reset_password_salt)
    token = s.dumps(
        dict(
            u=username,
            e=email))
    url = 'http://www.genitag.org/action/reset?token=' + token
    subject = 'Reset your Genitag password'
    message = 'visit this link to reset your password. This link expires in one hour. ' \
              + username + '\r\n' + 'link: ' + url
    send_email(message, subject, email)
    return None


def change_email(username, email):
    s = URLSafeSerializer(secret_key, salt=change_email_salt)
    token = s.dumps(
        dict(
            u=username,
            e=email))
    url = 'http://www.genitag.org/action/changeemail?token=' + token
    subject = 'Verify email for Genitag account'
    message = 'visit this link to verify your email address to the account with the username ' \
              + username + '\r\n' + 'link: ' + url
    send_email(message, subject, email)
    return None
