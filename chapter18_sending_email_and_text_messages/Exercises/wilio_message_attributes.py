#! python3
# twilio_message_attributes.py - Sends a message and prints its attributes.

from twilio.rest import Client

accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = Client(accountSID, authToken)

myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'

message = client.messages.create(
    body='Mr. Watson - Come here - I want to see you.',
    from_=myTwilioNumber,
    to=myCellPhone
)

print('to      =', message.to)
print('from_   =', message.from_)
print('body    =', message.body)
print('status  =', message.status)
print('created =', message.date_created)
print('sent    =', message.date_sent)
print('sid     =', message.sid)
