from flask import Flask, jsonify, request, session
from transformers import pipeline
from twilio.twiml.messaging_response import MessagingResponse

import src.functions as functions
import src.services as services

app = Flask(__name__)
app.secret_key = "@@##1234@@"

classifier = pipeline("zero-shot-classification")
USER_PROFILE_API_URL = "https://example.com/api/create_user_profile"

# @app.route('/bot', methods=['POST'])
# def bot():
# 	incoming_message = request.values.get('Body', '').strip()
# 	print(incoming_message)

# 	resp = MessagingResponse()
# 	msg = resp.message()

# 	if 'joke' in incoming_message:
# 		output = services.get_joke()

# 	elif 'greet' in incoming_message:
# 		output = 'Hello Hi'

# 	elif 'services' in incoming_message:
# 		services_list = services.service_options(0)
# 		print(services_list)
# 		output = services_list

# 	else:
# 		api_key = services.fetch_apikey('wolfram-alpha')
# 		if api_key == None:
# 			output = 'Wolfram API key is required to start chatting'
# 		else:
# 			output = services.chatbot(api_key, incoming_message)

# 	msg.body(output)
# 	return str(resp)


service_providers = {
    "Provider A": {
        "data_plans": {"1GB": 10, "5GB": 20, "10GB": 30},
        "voucher_prices": {"£10 Voucher": 10, "£20 Voucher": 20, "£50 Voucher": 50},
    },
    "Provider B": {
        "data_plans": {"2GB": 15, "10GB": 25, "20GB": 40},
        "voucher_prices": {"£15 Voucher": 15, "£25 Voucher": 25, "£50 Voucher": 50},
    },
}

user_data = {}
logging_in = False


@app.route("/bot", methods=["POST"])
def bot():
    global user_data
    incoming_message = request.values.get("Body", "").strip()
    phone_number = request.form.get("From").split(":")[1]

    resp = MessagingResponse()
    msg = resp.message()

    output = functions.create_profile(user_data, incoming_message, phone_number)

    msg.body(output)
    return str(resp)


if __name__ == "__main__":
    app.run()
