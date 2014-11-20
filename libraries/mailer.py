import smtplib
from email.mime.text import MIMEText


def send_email(message, subject, address):
    msg = MIMEText(
        message
    )
    msg['Subject'] = subject
    msg['From'] = "Genitag <noreply@genitag.org>"
    msg['To'] = address
    s = smtplib.SMTP('smtp.mandrillapp.com', 587)
    s.login('evanroman1@gmail.com', 'cB2hu92TtAgrvmFUj7eX4A')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
