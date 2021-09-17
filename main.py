import asyncio

from login_vk import vk_account
from utils import update_proxy


if __name__ == '__main__':
    proxy = []
    is_next = True
    while is_next:
        try:
            if len(proxy) == 0:
                proxy += update_proxy()
            loop = asyncio.new_event_loop()

            result = loop.run_until_complete(asyncio.wait_for(vk_account(proxy.pop().split(":")), 300_000))
        except Exception as e:
            print(e)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
