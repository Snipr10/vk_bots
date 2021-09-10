import time

import httpx
from onlinesimru import GetNumbers

from utils import ONLIM_SMS_KEY


numbers = GetNumbers(ONLIM_SMS_KEY)


def get_number(attempt=0):
    try:
        response = httpx.post("http://onlinesim.ru/api/getNum.php",
                              params={
                                  "apikey": ONLIM_SMS_KEY,
                                  "service": "vkcom",
                                  "number": True,
                                  "country": 7,
                                  "extension": False,
                                  "operator": "rostelecom"
                              }).json()
        print(response)
        id = response["tzid"]
        phone = response["number"]
    except Exception as e:
        try:
            print(response['response'])
        except Exception:
            pass
        print(e)
        id = None
        phone = None

    return phone, id


def get_key(id, attempt=0):
    code = None
    try:
        code = numbers.wait_code(id, timeout=60*3)
        if len(code) > 6:
            code = code[-4:]
    except Exception as e:
        time.sleep(60*2)

        # if attempt < 5:
        #     return get_key(id, attempt=attempt + 1)
        print("can not get code")
    completed_phone(id)
    return code


def completed_phone(id):
    try:
        numbers.close(id)
    except Exception as e:
        pass