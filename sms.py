import time

import requests

from utils import VAK_KEY


def get_number():
    try:
        response = requests.get("https://vak-sms.com/api/getNumber/",
                                params={
                                    "apiKey": VAK_KEY,
                                    "service": "vk",
                                    "country": "ru",
                                    "operator": "rostelecom"
                                }).json()
        print(response)
        id = response["idNum"]
        phone = str(response["tel"])
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
    response = requests.get("https://vak-sms.com/api/getBalance/",
                            params={
                                "apiKey": VAK_KEY,
                            }).json()
    balance = response.get("balance")
    return balance


def get_key(id, attempt=0):
    code = None
    try:
        if attempt > 6:
            completed_phone(id)
            return None
        response = requests.get("https://vak-sms.com/api/getSmsCode/",
                                params={
                                    "apiKey": VAK_KEY,
                                    "idNum": id,
                                    "all": ""
                                }).json()
        code = response.get("smsCode")
        if code is not None:
            if len(code) > 6:
                code = code[-4:]
        else:
            time.sleep(50)
            return get_key(id, attempt + 1)
    except Exception :
        time.sleep(1)
        print("can not get code")
    completed_phone(id)
    return code


def completed_phone(id):
    try:
        requests.get("https://vak-sms.com/api/setStatus/",
                     params={
                         "apiKey": VAK_KEY,
                         "idNum": id,
                         "status": "end"
                     })
    except Exception:
        pass
    try:
        requests.get("https://vak-sms.com/api/setStatus/",
                     params={
                         "apiKey": VAK_KEY,
                         "idNum": id,
                         "status": "end"
                     })
    except Exception:
        pass
