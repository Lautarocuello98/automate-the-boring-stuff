#! python3
# send_sms_twilio.py - Sends a text message using Twilio.

from twilio.rest import Client

# You get these from your Twilio account dashboard:
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

print(message.sid)
