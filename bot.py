import random
from flask import Flask, request
from pymessenger.bot import Bot

# app structure
app = Flask(__name__)
ACCESS_TOKEN = 'EAAN2ZCdubTVMBACgRyu1RtyxltQNWgKt713MMNlk6EzyGI5knRqEGTWWmUWsfs2dpPh3uoNQzu0lwGnhqvkmWVXdTjUbNbZAgbJjZAGDn5ZBOJVXCZBx4sUAVHjx9XvCZC5DhYTsQRMLLVhNxZBjG2vjI2frXwEZCMZBKfbZAIknoFU4AcKF4DwB8B'
VERIFY_TOKEN = 'CheeryBotty5@5'
bot = Bot(ACCESS_TOKEN)

#route
@app.route('/', methods=['GET', 'POST'])
#pages
def receive_msg():
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        return verify_fb_token(token_sent)
    else: #if the request is 'POST'
        output = request.get_json()
        for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('attachments'):
                    response_sent_nontext = get_video()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = [
        'poem1',
        'poem2',
        'poem3',
    ]
    # return selected item to the user
    return random.choice(sample_responses)

def get_video():
    return 'video placeholder'

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"



#runs the app
if __name__ == '__main__':
    app.run()