import json

import requests


def get_joke():
    url = "https://some-random-api.ml/joke"
    r = requests.get(url)
    data = r.json()
    print(data)
    return data["joke"]


def fetch_apikey(api):
    with open("data/credentials.json") as f:
        data = json.load(f)
    key = data.get(api, None)
    return data[api]


def chatbot(api_key, query):
    url = f"http://api.wolframalpha.com/v1/result?appid={api_key}&i={query}%3f"
    r = requests.get(url)
    data = r.text
    if data == "Wolfram|Alpha did not understand your input":
        return "Couldn't understand your query"
    else:
        return data


def service_options(s_type):
    s_list = ["Thank you for contacting us, please chose what you want to do today\n"]
    with open("data/services.json") as f:
        data = json.load(f)

    for item in data["service_list"]:
        for key, value in item.items():
            s_list.append(f"{key}. {value}\n")
    return "".join(s_list)


def create_user_profile_api(user_data):
    api_url = "http://localhost:4480/login/chat-try/create-account"
    headers = {"Content-Type": "application/json"}
    data = {
        "username": user_data["name"],
        "email": user_data["email"],
        "phone": user_data["phone_number"],
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for bad responses
        return "Profile created successfully!"
    except requests.exceptions.RequestException as e:
        # Handle API errors (e.g., log them)
        return "Error creating profile. Please try again later."


def login_api(user_data):
    api_url = "http://localhost:4480/login/chat-try/login"
    headers = {"Content-Type": "application/json"}
    data = {
        "username": user_data["name"],
        "password": user_data["password"],
        "phone": user_data["phone_number"],
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for bad responses
        return "Profile created successfully!"
    except requests.exceptions.RequestException as e:
        # Handle API errors (e.g., log them)
        return "Error creating profile. Please try again later."


# def get_data_list(provider):
