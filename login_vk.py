import asyncio
import datetime
import random

from dateutil.relativedelta import relativedelta
from scraper import BrowserManager, generate_cookie, join_save
from sms import get_number, get_key
from utils import TEXT_WIDTH, TEXT_HEIGHT, DEFAULT_TIMEOUT, get_name_sex, DEFAULT_SLEEP_WAIT, get_pass, \
    user_agents, NEW_PAGE_TIMEOUT, PASSWORD_GLASSEN, USERNAME_GLASSEN, save_bot

URL_JOIN = "https://vk.com/join"
GLASSEN_LOGIN_URL = "https://api.glassen-it.com/"
VK_BOT_URL = "https://api.glassen-it.com/component/socparser/bot/vkbotstart"


async def vk_account(proxy=None):
    async with BrowserManager(proxy) as browser_manager:

        browser = browser_manager.browser
        page = await browser.newPage()
        await page._client.send('Network.setCookies', {
            'cookies': generate_cookie(),
        })

        await page.authenticate({'username': proxy[2], 'password': proxy[3]})
        user_agent = random.choice(user_agents)

        await page.setViewport(
            {
                TEXT_WIDTH: user_agent.get(TEXT_WIDTH),
                TEXT_HEIGHT: user_agent.get(TEXT_HEIGHT)
            }
        )

        await page.setUserAgent(user_agent.get("userAgentData"))
        #GET cookies
        try:
            await asyncio.gather(
                page.goto("https://www.youtube.com/", timeout=NEW_PAGE_TIMEOUT),
                page.goto("https://www.amazon.com/", timeout=NEW_PAGE_TIMEOUT),
                page.goto("https://www.avito.ru/", timeout=NEW_PAGE_TIMEOUT),
                page.goto("https://translate.google.com/?hl=ru", timeout=NEW_PAGE_TIMEOUT),
                page.goto("https://www.instagram.com/?hl=ru", timeout=NEW_PAGE_TIMEOUT)
            )
        except Exception:
            pass
        await page.goto(URL_JOIN, timeout=NEW_PAGE_TIMEOUT)

        first_name, last_name, sex = get_name_sex()
        #USERNAME
        first_name_el = await page.waitForSelector("[name='first_name']", timeout=DEFAULT_TIMEOUT)
        await first_name_el.type(first_name)

        #PASSWORD
        last_name_el = await page.waitForSelector("[name='last_name']", timeout=DEFAULT_TIMEOUT)
        await last_name_el.type(last_name)


        # DATE BORN
        born_date = datetime.date.today() - datetime.timedelta(
            days=random.randint(0, 40)
        ) - relativedelta(
            months=random.randint(0, 11)
        ) - relativedelta(
            years=random.randint(18, 50)
        )
        day = born_date.day
        month = born_date.month
        year = born_date.year

        date_el = await page.querySelectorAll("[class='selector_input selected']")
        await date_el[0].type(str(day))
        await page.keyboard.press('Enter')

        await asyncio.sleep(2*DEFAULT_SLEEP_WAIT)
        await date_el[1].type("И")
        for i in range(month):
            await asyncio.sleep(DEFAULT_SLEEP_WAIT)
            await page.keyboard.press('ArrowDown')
        await page.keyboard.press('Enter')
        for i in range(month):
            await asyncio.sleep(DEFAULT_SLEEP_WAIT)
            await page.keyboard.press('ArrowUp')
        await asyncio.sleep(DEFAULT_SLEEP_WAIT)
        await page.keyboard.press('Enter')

        await asyncio.sleep(2*DEFAULT_SLEEP_WAIT)

        await date_el[2].type(str(year))
        await page.keyboard.press('Enter')
        await asyncio.sleep(DEFAULT_SLEEP_WAIT)

        await page.click("[class='FlatButton__content']", timeout=DEFAULT_TIMEOUT)

        #SEX
        try:
            sex_radio = await page.waitForSelector(f'[data-sex="{sex}"]', timeout=DEFAULT_TIMEOUT)
            await sex_radio.click()
            await page.click("[class='FlatButton__content']", timeout=DEFAULT_TIMEOUT)

        except Exception:
            pass

        #PHONE
        phone_number, id = get_number()
        if not phone_number:
            print("CAN NOT GET PHONE")
            return
        phone_el = await page.waitForSelector("#join_phone", timeout=DEFAULT_TIMEOUT)
        await phone_el.type(phone_number.replace("+7", ""))

        await page.click("#join_send_phone", timeout=DEFAULT_TIMEOUT)
        await page.waitForSelector("#join_code", timeout=DEFAULT_TIMEOUT)

        #CODE SMS
        code = get_key(id)
        print("SMS")
        print(code)

        phone_code_el = await page.waitForSelector("#join_code", timeout=DEFAULT_TIMEOUT)
        await asyncio.sleep(DEFAULT_SLEEP_WAIT)
        await phone_code_el.type(code)
        await asyncio.sleep(DEFAULT_SLEEP_WAIT)
        await page.waitForSelector("#join_send_code", timeout=DEFAULT_TIMEOUT)
        await asyncio.sleep(DEFAULT_SLEEP_WAIT)
        await page.click("#join_send_code", timeout=DEFAULT_TIMEOUT)

        print("PASSWORD")
        #PASSWORD
        await asyncio.sleep(3*DEFAULT_SLEEP_WAIT)

        pass_el = await page.waitForSelector("#join_pass", timeout=DEFAULT_TIMEOUT)
        password = get_pass()
        await pass_el.type(password)
        await page.click("#join_send_pass", timeout=DEFAULT_TIMEOUT)

        #SUCCES
        try:
            await asyncio.sleep(5 * DEFAULT_SLEEP_WAIT)

            await page.click("[class='flat_button button_wide button_big_text']", timeout=DEFAULT_TIMEOUT)
        except Exception:
            pass

        try:
            try:

                #country russia
                await asyncio.sleep(2*DEFAULT_SLEEP_WAIT)
                country = await page.waitForSelector("[class='selector_input selected']", timeout=DEFAULT_TIMEOUT)
                await country.type("Р")

                await page.keyboard.press('ArrowDown')
                await page.keyboard.press('Enter')

                #CITY
                await asyncio.sleep(4*DEFAULT_SLEEP_WAIT)
                city_el = await page.querySelectorAll("[class='selector_input']")
                city = random.randint(1, 1)
                await city_el[-1].type("Mосква")
                for i in range(city):
                    await page.keyboard.press('ArrowDown')
                await page.keyboard.press('Enter')
                try:
                    await join_save(page)
                except Exception:
                    pass

                # UNIVER
                await asyncio.sleep(10*DEFAULT_SLEEP_WAIT)
                univer_el = await page.querySelectorAll("[class='selector_input']")
                univer = random.randint(1, 6)
                await univer_el[-1].type("M")
                for i in range(univer):
                    await page.keyboard.press('ArrowDown')
                await page.keyboard.press('Enter')
                try:
                    await join_save(page)
                except Exception:
                    pass

                await asyncio.sleep(10*DEFAULT_SLEEP_WAIT)
                try:
                    univer_data_el = await page.querySelectorAll("[class='selector_input']")
                    for i in range(1, 5):
                        await asyncio.sleep(2 * DEFAULT_SLEEP_WAIT)
                        await univer_data_el[-1*i].type("")
                        for i in range(1, 7):
                            await page.keyboard.press('ArrowDown')
                        await page.keyboard.press('Enter')
                except Exception:
                    pass

                await page.click("#join_save", timeout=DEFAULT_TIMEOUT)

            except Exception:
                await page.click("[class='join_skip_link']", timeout=DEFAULT_TIMEOUT)

            #EMAIL
            try:
                #TODO without
                await asyncio.sleep(5*DEFAULT_SLEEP_WAIT)

                await page.click("#join_save", timeout=DEFAULT_TIMEOUT)
            except Exception:
                await page.click("[class='join_skip_link']", timeout=DEFAULT_TIMEOUT)
        except Exception as e:
            pass

        page_glassen = await browser.newPage()

        await page_glassen.authenticate({'username': proxy[2], 'password': proxy[3]})

        await page_glassen.goto(GLASSEN_LOGIN_URL, timeout=NEW_PAGE_TIMEOUT)
        usernameEl, passwordEl = await asyncio.gather(
            page_glassen.waitForSelector("#username", timeout=DEFAULT_TIMEOUT),
            page_glassen.waitForSelector("#password", timeout=DEFAULT_TIMEOUT)
        )
        await usernameEl.type(USERNAME_GLASSEN)
        await passwordEl.type(PASSWORD_GLASSEN)

        await asyncio.gather(
            page_glassen.waitForNavigation(timeout=NEW_PAGE_TIMEOUT),
            page_glassen.click("[class='uk-button uk-button-primary']", timeout=DEFAULT_TIMEOUT),
        )

        vk_page = await browser.newPage()
        await vk_page.authenticate({'username': proxy[2], 'password': proxy[3]})

        await vk_page.goto(VK_BOT_URL, timeout=NEW_PAGE_TIMEOUT)
        bot_usernameEl, bot_passwordEl = await asyncio.gather(
            vk_page.waitForSelector("#login", timeout=DEFAULT_TIMEOUT),
            vk_page.waitForSelector("#password", timeout=DEFAULT_TIMEOUT)
        )

        await bot_usernameEl.type(phone_number)
        await bot_passwordEl.type(password)
        await asyncio.gather(
            vk_page.waitForNavigation(timeout=NEW_PAGE_TIMEOUT),
            vk_page.click("[class='uk-button']", timeout=DEFAULT_TIMEOUT),
        )
        try:
            vk_bot_usernameEl, vk_bot_passwordEl = await asyncio.gather(
                vk_page.waitForSelector("[type='text']", timeout=DEFAULT_TIMEOUT),
                vk_page.waitForSelector("[type='password']", timeout=DEFAULT_TIMEOUT)
            )

            await vk_bot_usernameEl.type(phone_number)
            await vk_bot_passwordEl.type(password)

            await asyncio.gather(
                vk_page.waitForNavigation(timeout=NEW_PAGE_TIMEOUT),
                vk_page.click("[type='submit']", timeout=DEFAULT_TIMEOUT),
            )
        except Exception:
            pass
        try:
            await asyncio.gather(
                vk_page.waitForNavigation(timeout=NEW_PAGE_TIMEOUT),
                vk_page.click("[class='flat_button fl_r button_indent']", timeout=DEFAULT_TIMEOUT),
            )
        except Exception:
            pass

        save_bot(phone_number, password)
        return phone_number, password