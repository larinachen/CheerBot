from flask import Flask

# app structure
app = Flask(__name__)

#pages
def receive_msg():
    return "Message received!"