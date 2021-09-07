import random
import string

FINDING_ERROR_MESSAGES_TIMEOUT = 2 * 1000
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3419.0 Safari/537.36'
DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080
TEXT_WIDTH = "width"
TEXT_HEIGHT = "height"
ONE_SECOND_TIMEOUT = 1000
DEFAULT_TIMEOUT = 50 * ONE_SECOND_TIMEOUT
NEW_PAGE_TIMEOUT = 100 * ONE_SECOND_TIMEOUT

DEFAULT_SLEEP_WAIT = 2

ONLIM_SMS_KEY =
USERNAME_GLASSEN =
PASSWORD_GLASSEN =


def update_proxy():
    return get_data_from_doc("proxies.txt").split("\n")


def get_data_from_doc(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return data


def save_bot(phone_number, password):
    print(f"Bot add: {phone_number}")
    try:
        my_file = open(f"{phone_number}.txt", "w+")
        my_file.write(password)
        my_file.close()
    except Exception:
        pass


def get_name_sex():
    name = random.choice(names)
    last_name = random.choice(last_names)

    return name[0], last_name, name[1]


def get_pass(length=random.randint(6, 10)):
    password = ''.join(random.choice(string.ascii_uppercase) for i in range(int(length / 2)))
    return password.join(random.choice(string.ascii_lowercase) for i in range(int(length / 2)))


names = [("Александр", 1),
         ("Михаил", 1),
         ("Максим", 1),
         ("Артем", 1),
         ("Даниил", 1),
         ("Марк", 1),
         ("Иван", 1),
         ("Лев", 1),
         ("Дмитрий", 1),
         ("Матвей", 1),
         ("Роман", 1),
         ("Тимофей", 1),
         ("Кирилл", 1),
         ("Илья", 1),
         ("Никита", 1),
         ("Андрей", 1),
         ("Федор", 1),
         ("Егор", 1),
         ("Алексей", 1),
         ("Константин", 1),
         ("Владимир", 1),
         ("Ярослав", 1),
         ("София", 2),
         ("Мария", 2),
         ("Анна", 2),
         ("Алиса", 2),
         ("Виктория", 2),
         ("Полина", 2),
         ("Ева", 2),
         ("Елизавета", 2),
         ("Александра", 2),
         ("Анастасия", 2),
         ("Варвара", 2),
         ("Дарья", 2),
         ("Ксения", 2),
         ("Вероника", 2),
         ("Василиса", 2),
         ("Арина", 2),
         ("Екатерина", 2),
         ("Милана", 2),
         ("Екатерина", 2),
         ("Кира", 2),
         ("Валерия", 2),
         ("Мирослава", 2),
         ("Ульяна", 2),
         ("Вера", 2),
         ("Амина", 2),
         ("Таисия", 2),
         ]
last_names = ["Гусь", "Лось", "Крот", "Холод", "Царь", "Князь", "Шабан", "Юсуп", "Бык"]

user_agents = [{
    "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1683 Yowser/2.5 Safari/537.36",
    "width": 1360,
    "height": 768
},
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.1.2924.93 FreeU/56.1.2924.93 MRCHROME SOC Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35 (Edition Yx 01)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 YaBrowser/13.10.1500.9323 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 YaBrowser/15.9.2403.2966 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.721 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 OPR/44.0.2510.857 (Edition Campaign 34)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/55 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.721 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.724 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.38 Safari/537.36 OPR/49.0.2725.18 (Edition beta)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55 (Edition 360)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/66.4.134 Chrome/60.4.3112.134 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36 OPR/49.0.2725.34",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.2052 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.851 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.851 Yowser/2.5 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Campaign 34)",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition 360-1)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.2017 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1686 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.719 Yowser/2.5 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.719 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2950.1 Iron Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/538.12.28 (KHTML, like Gecko) Chrome/59.0.3086.66 Safari/538.12.28",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.69.1021 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/49.13.20.400 Chrome/49.0.2623.110 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.138 Safari/537.36 Vivaldi/1.8.770.56",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36 OPR/46.0.2597.32",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Campaign 75)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.89 Chrome/62.0.3202.89 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3200.0 Iron Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Campaign 67)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 4.10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2130.80",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.850 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.828 Yowser/2.5 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.21 Safari/537.36 MMS/1.0.2531.0",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.850 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.792 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Yx)",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Yx)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.791 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3223.8 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.882",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2083 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Ask)",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.91 Safari/537.36 Vivaldi/1.92.917.39",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.725 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3218.0 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:54.0) Gecko/20100101 Firefox/54.0",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36 Vivaldi/1.93.955.48",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 YaBrowser/17.1.0.2034 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 SputnikBrowser/3.1.1485.1 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/7.0.6.1042 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3213.3 Safari/537.36 OPR/50.0.2729.0 (Edition developer)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.40 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.3.3029.81 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 YaBrowser/15.9.2403.3043 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2130.80 (Edition Yx)",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.18 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47 (Edition Yx)",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.826 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.888",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.1512 (beta) Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.828 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1686 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39 (Edition Campaign 75)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2130.80",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.721 Yowser/2.5 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.797 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39 (Edition Yx)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.59 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39 (Edition Campaign 34)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.62 Chrome/62.0.3202.62 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3260.2 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 OPR/44.0.2510.1218",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3269.3 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Yx)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:52.9) Gecko/20100101 Goanna/3.4 Firefox/52.9 PaleMoon/27.6.0",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.2017 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/17.0.558.0 Safari/534.31 UCBrowser/3.4.3.532",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 YaBrowser/16.2.0.3539 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; CrOS aarch64 9765.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.123 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47 (Edition Yx)",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1686 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Campaign 76)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; CrOS x86_64 9592.96.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.114 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35 (Edition Campaign 34)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.919 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition 360-1)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Campaign 34)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 YaBrowser/14.10.2062.12061 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.1.2924.93 FreeU/56.1.2924.93 MRCHROME SOC Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.89 Safari/537.36 42885",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 OPR/41.0.2353.46",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/62.0.3192.0 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Yx)",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.150 Amigo/58.0.3029.150 MRCHROME SOC Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.137",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.919 Yowser/2.5 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 OPR/38.0.2220.29 (Edition Campaign 34)",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 OPR/37.0.2178.54",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.92 Safari/537.36 42885",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2081 Yowser/2.5 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36 OPR/39.0.2256.48",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.197 Amigo/56.0.2924.197 MRCHROME SOC Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.791 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 YaBrowser/15.2.2214.3645 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3269.3 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; rv:57.0) Gecko/20100101 Firefox/57.0",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47 (Edition Campaign 32)",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.852 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.888",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3260.2 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55 (Edition Yx)",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux i686; rv:57.0) Gecko/20100101 Firefox/57.0",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.898",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.39",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 UBrowser/7.0.69.1021 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.2017 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; rv:57.0) Gecko/20100101 Firefox/57.0",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.797 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39 (Edition Campaign 34)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.0.1633 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39 (Edition Campaign 76)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39 (Edition Yx)",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.69.1022 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.797 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Campaign 34)",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Campaign 34)",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36 OPR/49.0.2725.34",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.824 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Campaign 34)",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3253.3 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.961 Yowser/2.5 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3266.1 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.1.2924.82 FreeU/56.1.2924.82 MRCHROME SOC Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.150 Amigo/58.0.3029.150 MRCHROME SOC Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50 (Edition Campaign 76)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144 (Edition Rambler)",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; CrOS x86_64 9765.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.123 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition Yx)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.1.2909.1213 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57 (Edition 360-1)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.1512 (beta) Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 OPR/41.0.2353.46 (Edition Campaign 34)",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52 (Edition 360-1)",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2130.80 (Edition Campaign 09)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.532 (beta) Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.797 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.852 Yowser/2.5 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 OPR/36.0.2130.32",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.831 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.768 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39 (Edition Campaign 34)",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3218.0 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.831 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.768 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39 (Edition Campaign 34)",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64; rv:52.9) Gecko/20100101 Goanna/3.3 Firefox/52.9 PaleMoon/27.5.0",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39 (Edition Yx)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Campaign 34)",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 YaBrowser/14.10.2062.12521 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.824 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.850 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.898",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2081 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.768 Yowser/2.5 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.828 Yowser/2.5 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.768 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35 (Edition Campaign 34)",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.850 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; rv:56.0) Gecko/20100101 Firefox/56.0",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35 (Edition Yx)",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.828 Yowser/2.5 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.92 Safari/537.36 42885",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.0.12195 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36 OPR/46.0.2597.26314",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2909.1213 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.1.768 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39 (Edition Yx)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3213.3 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1104.222 YaBrowser/1.5.1104.222 Safari/537.4",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80 (Edition Campaign 34)",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2081 Yowser/2.5 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2081 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36 OPR/48.0.2685.32",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.137",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition Yx)",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.804 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2081 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.955 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Iridium/58.0 Safari/537.36 Chrome/58.0.3029.81",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.804 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.804 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.792 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.1026 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.835 (beta) Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1683 Yowser/2.5 Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.726 Yowser/2.5 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81 (Edition Yx)",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.804 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.792 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; rv:54.0) Gecko/20100101 Firefox/54.0",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows; rv:52.0) Gecko/20100101 Firefox/52.0",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.791 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.840 Yowser/2.5 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55 (Edition Yx 01)",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71 (Edition 360-1)",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.724 Yowser/2.5 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.791 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.791 Yowser/2.5 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1683 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.719 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "width": 1280,
        "height": 800
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.1.791 Yowser/2.5 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; rv:53.0) Gecko/20100101 Firefox/53.0",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 YaBrowser/17.7.0.1544 Yowser/2.5 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.197 Amigo/56.0.2924.197 MRCHROME SOC Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1024,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1360,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.2081 Yowser/2.5 Safari/537.36",
        "width": 1536,
        "height": 864
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.197 Amigo/56.0.2924.197 MRCHROME SOC Safari/537.36",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.7.3029.81 Safari/537.36",
        "width": 1280,
        "height": 1024
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "width": 1920,
        "height": 1080
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 YaBrowser/15.9.2403.3043 Safari/537.36",
        "width": 1680,
        "height": 1050
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 YaBrowser/17.10.0.2017 Yowser/2.5 Safari/537.36",
        "width": 1440,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39 (Edition Yx)",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.39",
        "width": 2560,
        "height": 1440
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1600,
        "height": 900
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.52 Safari/537.36",
        "width": 1280,
        "height": 720
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80",
        "width": 1920,
        "height": 1200
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "width": 1366,
        "height": 768
    },
    {
        "userAgentData": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "width": 1280,
        "height": 1024
    }
]
