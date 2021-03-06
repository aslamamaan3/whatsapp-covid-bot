from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
import re

app = Flask(__name__)


@app.route("/")
def hello():
		return "Hello World"

@app.route("/covidbot", methods=['POST'])

def covidBot():
	receivedMsg = request.values.get('Body', '').lower()
	response = MessagingResponse()
	message = response.message()
	responded = False

	regexTest = re.search("^covid country ", receivedMsg)

	if regexTest != None:

		country = receivedMsg[13:]
		country = country.strip()
		print(country)

		r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/' + country)

		if r.status_code == 200:

			try:
				data = r.json()
				msgText = f'Country: *{data["country"]}* \nTotal Cases: *{data["cases"]}* \nCases Today: *{data["todayCases"]}* \n\nTotal Deaths: *{data["deaths"]}* \nDeaths Today: *{data["todayDeaths"]}* \n\nRecovered: *{data["recovered"]}*'
				message.body(msgText)
			except ValueError as e:
				message.body('Country not found.')

		else:
			message.body('Service unavailable at this time.')

		responded = True

	else:
		message.body('Wrong Command. Please use - covid country countryname')
		responded = True	


	if responded == False:
		return

	return str(response)



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)