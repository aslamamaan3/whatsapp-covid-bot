from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)


@app.route("/")
def hello():
		return "Hello World"


@app.route("/covidbot", methods=['POST'])

def covidBot():
	receivedMsg = request.values.get('Body', '')
	response = MessagingResponse()
	message = response.message()
	responded = False

	if receivedMsg.find("covid country ", 0, 13) != -1

		country = receivedMsg[14:]
		country = country.strip()

		r = request.get('https://coronavirus-19-api.herokuapp.com/countries/' + country)

		if r.status_code = 200
			data = json.loads(r)
			msgText = 'Country: ' +data["country"] + '\nTotal Cases: ' +data["cases"] + '\nCases Today: ' +data["todayCases"] + '\n\nTotal Deaths' +data["deaths"]+ '\nDeaths Today' +data["todayDeaths"]+ '\nRecovered:' + data["recovered"] 		
			message.body(msgText)
		else
			message.body('Service unavailable at this time')

		responded = True


	if responded == False
		return

	return str(response)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)