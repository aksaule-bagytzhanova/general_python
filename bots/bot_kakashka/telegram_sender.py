from pprint import pprint

import requests

TOKEN = "2096075563:AAGoruekIr7b-9s39cPU4kJLtVeKmRkyzqE"
CHANNEL = "@sulaksi"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHANNEL}&text="


def send_message(text):
    response = requests.get(f"{URL}{text}")
    if response.status_code == 200:
        pprint(response.json())
    else:
        print(response.text)

