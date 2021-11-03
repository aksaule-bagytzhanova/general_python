# import requests
# from bs4 import BeautifulSoup as BS
# from requests.models import Response

# r = requests.get("https://leetcode.com/desalichka/")
# soup = BS(Response.content, 'html.parser')
# data = soup.find('span', {'class_':'difficulty-ac-count__jhZm'}).text
# print(data)

import requests
from bs4 import BeautifulSoup

def get_ot():
    headers = {
        'user-agent' : "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36"
    }

    url = "https://leetcode.com/desalichka/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    block_ot = soup.find_all("div", class_="total-solved-container__1WZP")
    for ot in block_ot:
        ot_title = ot.find("span", class_="difficulty-ac-count__jhZm").text.strip()
        print(ot_title)