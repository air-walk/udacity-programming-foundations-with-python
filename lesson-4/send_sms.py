# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC0000000000000000000000000000"
auth_token  = "e000000000000000000000000"
client      = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+18888888888",
                                             from_="+19999999999",
                                             body="Greetings!")
