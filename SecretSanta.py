# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random
import time

# TWILIO NUMBER 1234567890
account_sid = 'accountSID goes here'
auth_token = 'account token goes here'
client = Client(account_sid, auth_token)

phonebook = {'Grandpa':'1234567890', 'Aunt':'1234567890', 'Brother':'1234567890', 'Mom':'1234567890',
'Dad':'1234567890', 'Uncle':'1234567890', 'Uncle':'1234567890'}

def send_text(phonenumber, message):
    message = client.messages \
                .create(
                     body= message,
                     from_='1234567890',
                     to=phonenumber
                 )
    print('Message sent to ', phonenumber)


#ask = input('Who is all in the drawing? (enter a comma seperated list) ')
drawers = phonebook.keys()
bowl = list(drawers)

def run():
    if (len(drawers)) > 1:
        for picker in drawers:                  
            #for each person, draw a random name from the list.
            match = random.choice(bowl)
            #while the name you draw is your name
            while match == picker and len(drawers) > 1:
                #draw another name
                match = random.choice(bowl)
            #delete tha name that you drew from the list
            bowl.remove(match)
            send_text(phonebook.get(picker), match)
