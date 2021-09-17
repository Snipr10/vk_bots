import logging
import os
import random

from pyppeteer import launch

from chromium import set_chromium_version
from utils import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_TIMEOUT


class BrowserManager:

    def __init__(self, proxy=None, **kargs):
        self.browser = None
        self.proxy = proxy
        self.params = kargs

    async def __aenter__(self):
        set_chromium_version("839847")
        headless = os.getenv('HEADLESS', 'true').lower() == 'true'
        self.browser = await launch(headless=headless,
                                    handleSIGINT=False,
                                    handleSIGTERM=False,
                                    handleSIGHUP=False,
                                    args=[
                                        "--no-sandbox",
                                        f"--window-size={DEFAULT_WIDTH},{DEFAULT_HEIGHT}",

                                        f'--proxy-server={self.proxy[0]}:{self.proxy[1]}'
                                    ])
        # await page.authenticate({'username': 'KWE18Q', 'password': 'y08j96'})
        return self

    async def __aexit__(self, type, value, traceback):
        if self.browser:
            await self.browser.close()


async def get_cookies(page):
    return await page._client.send('Network.getAllCookies')


async def join_save(page):
    await page.click("#join_save", timeout=DEFAULT_TIMEOUT)


def generate_cookie():
    return [
        {
            'name': 'tt_webid_v2',
            'value': str(random.randint(10000, 999999999)),
            'domain': '.tiktok.com',
            'path': '/',
            'expires': -1,
            'size': 49,
            'httpOnly': False,
            'secure': True,
            'session': True
        },
        {
            'name': 's_v_web_id',
            'value': 'verify_khgp4f49_V12d4mRX_MdCO_4Wzt_Ar0k_z4RCQC9pUDpX',
            'domain': '.tiktok.com',
            'path': '/',
            'expires': -1,
            'size': 49,
            'httpOnly': False,
            'secure': True,
            'session': True
        },

        {
            'name': 'VID',
            'value': '08_6uN0ekdI400000W10H424:::0-0-0-64d8dec:CAASENr85ZWh9kj6K0tIoQ9lTesaYCO8h0CmbdH3tdh3FsQCwH2oqTJoy4E7ZVGLhfyFqKBXF3WpUfz8gQKcCQAfyA-OMeQmSzEHEvMJiVOkfPc5FjcLjLCy04Jy_i5kQK34BiqNEGdzY6pGZ4J6Dw3pm7h3hQ',
            'domain': '.mail.ru',
            'path': '/',
            'expires': 1662368302.914116,
            'size': 202,
            'httpOnly': True,
            'secure': False,
            'session': False
        },
        {'name': 'hllc', 'value': '1', 'domain': '.relap.info', 'path': '/', 'expires': 1630832302.412159, 'size': 5,
         'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'suid', 'value': '4739aea9961e1fc514e6af9fa3fa9e94bcb68a37--fa7bb237d6c3f051b09c926c3cdf03d75f676a13',
         'domain': '.relap.info', 'path': '/', 'expires': -1, 'size': 86, 'httpOnly': True, 'secure': True,
         'session': True},
        {'name': 'fsts', 'value': '1630745902', 'domain': '.relap.info', 'path': '/', 'expires': 1946105902.412037,
         'size': 14, 'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'unique', 'value': 'chfRC6T6', 'domain': '.relap.info', 'path': '/', 'expires': 1946105902.411984,
         'size': 14, 'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'yabs-sid', 'value': '510695541630745901', 'domain': 'mc.yandex.ru', 'path': '/', 'expires': -1,
         'size': 26, 'httpOnly': False, 'secure': False, 'session': True}, {'name': 'i',
                                                                            'value': '0+TevIG5EZaVM0VprK4qFUlMwNnOyWQ1S5H7ie+txMGCX/sSbH5W9o43730LuWcFgTbWnGyJPkaCAMmTIAAtObWtQr8=',
                                                                            'domain': '.yandex.ru', 'path': '/',
                                                                            'expires': 1693817900, 'size': 93,
                                                                            'httpOnly': True, 'secure': True,
                                                                            'session': False},
        {'name': 's', 'value': 'ww=800|wh=600|fver=0', 'domain': '.mail.ru', 'path': '/', 'expires': 1662281900.918499,
         'size': 21, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'i', 'value': 'AQArNTNhAwBdBgUCAQC9BwgEAbgVAYkNBQIBAA==', 'domain': '.mail.ru', 'path': '/',
         'expires': 1646297900.918428, 'size': 41, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'sid', 'value': 'e8f25047f136d55a7f23b14d84ea7d5e', 'domain': 'suggests.go.mail.ru', 'path': '/',
         'expires': -1, 'size': 35, 'httpOnly': False, 'secure': False, 'session': True},
        {'name': 'ymex', 'value': '1946105901.yrts.1630745901', 'domain': '.yandex.ru', 'path': '/',
         'expires': 1662281901.92896, 'size': 30, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'session-token',
         'value': 'mSnr38Rh1GXB3G3uVkQZAwp+GH8k75fKbKgJvNK+94kJeoKTvnLuW0H7tub7mcf9a8DlLUrF99HpHSS1AAzHa0kDTjf7X5/pBxsF/XQ6AxebUCxawS2FBaibDQ4WD7LzHYnv3M5+4cibw0Z3vIqL8dHy9bBjH0X+gPgBtq+ek55IKqcsp7iK5FMD27gkLGA7vzO/nH2qHdLk9oTW0zZHmo/I25p6FpfkuD+pg+tfThWslxYE6I0zlqyvpjCeOLHh',
         'domain': '.amazon.com', 'path': '/', 'expires': 1662281898.236307, 'size': 269, 'httpOnly': False,
         'secure': True, 'session': False},
        {'name': 'tmr_lvid', 'value': '568e675381deca179838dfa7bc21abd7', 'domain': '.mail.ru', 'path': '/',
         'expires': 1659517100, 'size': 40, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'tmr_reqNum', 'value': '6', 'domain': '.mail.ru', 'path': '/', 'expires': 1659517100, 'size': 11,
         'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'lsts', 'value': '1630745902', 'domain': '.relap.info', 'path': '/', 'expires': 1946105902.412084,
         'size': 14, 'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'p', 'value': 'jWgAANZfhgAA', 'domain': '.mail.ru', 'path': '/', 'expires': 1693817899.909737,
         'size': 13, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'mrcu', 'value': 'B1726133352B43184CA6921091C0', 'domain': '.mail.ru', 'path': '/',
         'expires': 1946105899.722066, 'size': 32, 'httpOnly': True, 'secure': True, 'session': False}, {'name': 'mtrc',
                                                                                                         'value': '%7B%22mytrackerid%22%3A58519%2C%22tmr_lvid%22%3A%22568e675381deca179838dfa7bc21abd7%22%7D',
                                                                                                         'domain': '.mail.ru',
                                                                                                         'path': '/',
                                                                                                         'expires': 1631350700,
                                                                                                         'size': 93,
                                                                                                         'httpOnly': False,
                                                                                                         'secure': True,
                                                                                                         'session': False,
                                                                                                         'sameSite': 'Strict'},
        {'name': 'act', 'value': 'c8ab5ab6597740a6af879d9002c771a4', 'domain': '.mail.ru', 'path': '/', 'expires': -1,
         'size': 35, 'httpOnly': True, 'secure': True, 'session': True},
        {'name': 'searchuid', 'value': '2150415801630745900', 'domain': '.mail.ru', 'path': '/',
         'expires': 1946105900.755411, 'size': 28, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': '1P_JAR', 'value': '2021-09-04-08', 'domain': '.google.com', 'path': '/', 'expires': 1633337899.466798,
         'size': 19, 'httpOnly': False, 'secure': True, 'session': False}, {'name': 'NID',
                                                                            'value': '222=E9Xf5bMJfLOSatHshfTeCaA92UlnD67hbzSJTSUxGj5tKEeLpa85qSm6S_6dODuS45axJi5KdrEabChDKIR30xf6wAFXaWWNzhfeSZSC7ZLbV68Q0_n7a6IC7-KqDAsr9rOXJVQaP5I5LYKN05xIymzAu04TdpKqQrGrr49hv80',
                                                                            'domain': '.google.com', 'path': '/',
                                                                            'expires': 1646557098.922172, 'size': 178,
                                                                            'httpOnly': True, 'secure': True,
                                                                            'session': False},
        {'name': 'b', 'value': 'uUkBAAC4n1oBAQAC', 'domain': '.mail.ru', 'path': '/', 'expires': 1662281902.254026,
         'size': 17, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'ubid-main', 'value': '134-3402948-9394853', 'domain': '.amazon.com', 'path': '/',
         'expires': 1662281898.236255, 'size': 28, 'httpOnly': False, 'secure': True, 'session': False},
        {'name': 'abid', 'value': '42bdd803-d574-25ed-b517-35e3fe6bb61a', 'domain': '.associates-amazon.com',
         'path': '/', 'expires': 1633165097.7892, 'size': 40, 'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'i18n-prefs', 'value': 'USD', 'domain': '.amazon.com', 'path': '/', 'expires': 1662281896.635507,
         'size': 13, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'yandexuid', 'value': '2150415801630745900', 'domain': '.yandex.ru', 'path': '/',
         'expires': 1946105901.928918, 'size': 28, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'csm-hit', 'value': 'tb:s-GP15XA1JPE9QE5ZVYDZS|1630745896820&t:1630745897479&adb:adblk_no',
         'domain': 'www.amazon.com', 'path': '/', 'expires': 1660985897, 'size': 75, 'httpOnly': False, 'secure': False,
         'session': False},
        {'name': 'tmr_lvidTS', 'value': '1630745900354', 'domain': '.mail.ru', 'path': '/', 'expires': 1659517100,
         'size': 23, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'session-id-time', 'value': '2082787201l', 'domain': '.amazon.com', 'path': '/',
         'expires': 1662281898.236349, 'size': 26, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'skin', 'value': 'noskin', 'domain': '.amazon.com', 'path': '/', 'expires': -1, 'size': 10,
         'httpOnly': False, 'secure': False, 'session': True},
        {'name': 'FTID', 'value': '1XCpKi12m-e91XCpKi000LSx', 'domain': '.yadro.ru', 'path': '/',
         'expires': 1662238800.282604, 'size': 28, 'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'tt_webid_v2', 'value': '900165471', 'domain': '.tiktok.com', 'path': '/', 'expires': -1, 'size': 20,
         'httpOnly': False, 'secure': True, 'session': True},
        {'name': 'VID', 'value': '16NbZB2Bv1e91XCpKi000Lb9', 'domain': '.yadro.ru', 'path': '/',
         'expires': 1662238800.410983, 'size': 27, 'httpOnly': True, 'secure': True, 'session': False},
        {'name': 'yabs-vdrf', 'value': 'A0', 'domain': '.an.yandex.ru', 'path': '/', 'expires': 1631350701.415873,
         'size': 11, 'httpOnly': False, 'secure': False, 'session': False},
        {'name': 'session-id', 'value': '147-7932054-5040524', 'domain': '.amazon.com', 'path': '/',
         'expires': 1662281898.236387, 'size': 29, 'httpOnly': False, 'secure': True, 'session': False},
        {'name': 's_v_web_id', 'value': 'verify_khgp4f49_V12d4mRX_MdCO_4Wzt_Ar0k_z4RCQC9pUDpX', 'domain': '.tiktok.com',
         'path': '/', 'expires': -1, 'size': 62, 'httpOnly': False, 'secure': True, 'session': True},
        {'name': 'sp-cdn', 'value': '"L5Z9:RU"', 'domain': '.amazon.com', 'path': '/', 'expires': 1662281896.635544,
         'size': 15, 'httpOnly': True, 'secure': True, 'session': False}]


async def get_cookies(page):
    return await page._client.send('Network.getAllCookies')
