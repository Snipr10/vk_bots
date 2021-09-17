import time

import requests

from utils import SMS_5SIM_KEY

HEADERS = {
    "Accept": "application/json",
    "Authorization": f"Bearer {SMS_5SIM_KEY}"
}


def get_number():
    try:
        response = requests.get("https://5sim.net/v1/user/buy/activation/russia/any/vkontakte",
                                headers=HEADERS).json()
        print(response)
        id = response["id"]
        phone = str(response["phone"])
    except Exception as e:
        try:
            print(response['response'])
        except Exception:
            pass
        print(e)
        id = None
        phone = None

    return phone, id


def get_balance():
    balance = requests.get("https://5sim.net/v1/user/profile",
                           headers=HEADERS
                           ).json().get("balance", 0)
    return balance


def get_key(id, attempt=0):
    code = None
    try:
        if attempt > 6:
            completed_phone(id)
            return None
        response = requests.get(f"https://5sim.net/v1/user/check/{id}",
                                headers=HEADERS).json()
        try:
            print("code_json " + str(response))
            code = response.get("sms")[-1].get("code")
        except Exception:
            code = None
        if code is None:
            time.sleep(50)
            return get_key(id, attempt + 1)
    except Exception:
        time.sleep(1)
        print("can not get code")
    completed_phone(id)
    print("KEY: " + str(code))
    return code


def completed_phone(id):
    try:
        requests.get(f"https://5sim.net/v1/user/cancel/{id}",
                     headers=HEADERS).json()
    except Exception:
        pass
    try:
        requests.get(f"https://5sim.net/v1/user/finish/{id}",
                     headers=HEADERS).json()
    except Exception:
        pass
