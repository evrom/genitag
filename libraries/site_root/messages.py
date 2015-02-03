from libraries.mailer import send_email
from libraries.signer import sign_message


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
