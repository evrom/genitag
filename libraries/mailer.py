import mandrill
from configuration import config

api_key = config['app']['MANDRILL_API_KEY']


def send_email(message, subject, address):
    try:
        mandrill_client = mandrill.Mandrill(api_key)
        message = {'auto_html': True,
                   'from_email': 'noreply@genitag.org',
                   'from_name': 'No Reply',
                   'subject': subject,
                   'text': message,
                   'to': [{'email': address,
                           'type': 'to'}]}
        mandrill_client.messages.send(
            message=message,
            async=False)
    except:
        print('A mandrill error occurred')
        raise
