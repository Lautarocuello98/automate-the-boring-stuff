#! python3
# text_myself.py - Defines the textmyself() function that text a message passed tto it a string.

# Present values:
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+155559998888'
twilio_number = '+155555222567'

from twilio.rest import Client

def text_myself(message):
    twilio_cli = Client(account_sid, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)
    