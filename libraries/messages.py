from libraries.mailer import send_email
from libraries.signer import sign_message, sign_timed_message


def new_user(username, email):
    token = sign_message(
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
    token = sign_timed_message(
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
    token = sign_message(
        dict(
            u=username,
            e=email))
    message = "To change your email to " + email +\
              " go to: " + \
              "http://genitag.org/action/changeemail?token=" + token

    subject = "Change Genitag Email"
    send_email(message, subject, email)
    return None
