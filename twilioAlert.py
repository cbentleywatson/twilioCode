import twilio
import twilio.rest
from twilio.rest import Client



from twilio.rest import TwilioRestClient
accountSID = 'AC17a10d775bd21e2645cc0f00c04a9a57'
authToken = 'aa46d606b37bceda5d6cb067418a00e7'
client = Client(accountSID, authToken)
#twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+13213514328'
#myTwilioNumber = '+14955551234'
myCellPhone = '+13213606959'
message = client.messages \
    .create(
         body='Finished Program',
         from_=myTwilioNumber,
         to=myCellPhone
     )

print(message.sid)


#message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
