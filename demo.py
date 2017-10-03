from twilio.rest import Client
from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def send_sms(recipient, message):
    account_sid = environ.get("TWILIO_ACCOUNT_SID")
    auth_token = environ.get("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    client.messages.create(to=recipient, from_=environ.get("TWILIO_SENDER"), body=message)
    print('Message "{}" envoyé à {}.'.format(message, recipient))


def main():
    send_sms('+15815782355', 'Hello, world')

if __name__ == '__main__':
    main()
