import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import src.services as services


app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
	incoming_message = request.values.get('Body', '').strip()
	print(incoming_message)

	resp = MessagingResponse()
	msg = resp.message()

	if 'joke' in incoming_message:
		output = services.get_joke()

	elif 'greet' in incoming_message:
		output = 'Hello Hi'

	elif 'services' in incoming_message:
		services_list = services.service_options(0)
		print(services_list)
		output = services_list

	else:
		api_key = services.fetch_apikey('wolfram-alpha')
		if api_key == None:
			output = 'Wolfram API key is required to start chatting'
		else:
			output = services.chatbot(api_key, incoming_message)
	
	msg.body(output)
	return str(resp)

if __name__ == '__main__':
	app.run() 