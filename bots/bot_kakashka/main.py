from aiogram import Bot, executor, types
from config import token
import requests
from pprint import pprint
from bs4 import BeautifulSoup

# bot = Bot(token=token)
# dp = Displatcher(bot)


def get_data(url):
    headers = {'user-agent' : "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36"
}

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.text, "lxml")
    totals = soup.find_all('div', class_='total-solved-container__1WZP')
    
    for total in totals:
        easy_o = "https://leetcode.com/desalichka/" + total.find("div", class_='css-57z4bo-StatisticWrapper').find('span')
        print(easy_o)


# @dp.message_handler(commands='kaka')
# async def get_kaka(message: types.Message):
#     with open("")


get_data("https://leetcode.com/desalichka/")