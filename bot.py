from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)


@app.route("/")
def hello():
		return "Hello World"





if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)