from transformers import pipeline

import src.services as services

classifier = pipeline("zero-shot-classification")

creating_profile = False
loggin_in = False


def create_profile(user_data, incoming_message, phone_number):
    global creating_profile
    if creating_profile:
        # Handle profile creation steps
        if "name" not in user_data:
            user_data["phone_number"] = phone_number
            user_data["name"] = incoming_message
            output = "Please enter your email address:"
        elif "email" not in user_data:
            user_data["email"] = incoming_message
            output = "Please enter your email password:"
        elif "password" not in user_data:
            user_data["password"] = incoming_message
            output = services.create_user_profile_api(user_data)
            user_data = {}
            creating_profile = False
        else:
            creating_profile = False
            output = "Invalid input. Please start again."
    else:
        # Perform zero-shot classification only if not creating profile
        candidate_labels = ["create profile", "other"]
        result = classifier(incoming_message, candidate_labels)
        prompt = result["labels"][0]
        if prompt == "create profile":
            if "name" not in user_data:
                creating_profile = True
                user_data["phone_number"] = phone_number  # Store phone number first
                output = "Welcome to ChatBee \nCreate your account \n\nPlease enter your name:"
    return output


# def login_to_account(user_data, incoming_message, phone_number):
#     global loggin_in
#     if loggin_in:
#         # Handle profile creation steps
#         if "name" not in user_data:
#             user_data["phone_number"] = phone_number
#             user_data["name"] = incoming_message
#             output = "Please enter your password:"
#         elif "password" not in user_data:
#             user_data["password"] = incoming_message
#             output = services.login_api(user_data)
#             # user_data = {}
#             loggin_in = False
#         else:
#             output = services.login_api(user_data)
#             loggin_in = False
#             # output = "Invalid input. Please start again."
#     else:
#         # Perform zero-shot classification only if not creating profile
#         candidate_labels = ["login", "other"]
#         result = classifier(incoming_message, candidate_labels)
#         prompt = result["labels"][0]
#         if prompt == "login":
#             if "name" not in user_data:
#                 loggin_in = True
#                 user_data["phone_number"] = phone_number  # Store phone number first
#                 output = "Welcome to ChatBee \nLogin to start your session \n\nPlease enter your name:"
#             # else:
#             #     output = services.login_api(user_data)
#     return output
