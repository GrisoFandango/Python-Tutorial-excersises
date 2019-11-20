# Twilio has an useful package to make it easier to access the API
from twilio.rest import Client
import setting

# creating a variable to pass the authorization information for the API
client = Client(setting.account_sid, setting.auth_token)
# With the following lines we can send a text message from twilio
client.messages.create(
    to="...",  # number where we want send a message
    # number from where we send message (the one on Twilio)
    from_="...",
    body="This is my first test message"  # Content of the message
)
