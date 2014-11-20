from libraries.signer import sign_message
from libraries.mailer import send_email


def change_email(username, email):
    token = sign_message(
        dict(
            username=username,
            email=email))
    message = "To change your email to " + email +\
              " go to: " + \
              "http://genitag.org/action/changeemail?token=" + token

    subject = "Change Genitag Email"
    send_email(message, subject, email)
    return None
