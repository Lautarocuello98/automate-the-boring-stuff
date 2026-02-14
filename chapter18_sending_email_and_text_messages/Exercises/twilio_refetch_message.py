#! python3
# twilio_refetch_message.py - Sends a message, then refetches it to get updated status.

import time
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

print('Initial status:', message.status)
print('Initial date_sent:', message.date_sent)
print('SID:', message.sid)

# Wait a bit so Twilio can process delivery.
time.sleep(5)

updatedMessage = client.messages.get(message.sid)
print('Updated status:', updatedMessage.status)
print('Updated date_sent:', updatedMessage.date_sent)
