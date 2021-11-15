import time
from datetime import date

import schedule

from bots.bot_kakashka.leetcode_parser import get_profile
from bots.bot_kakashka.telegram_sender import send_message

sula_username = 'desalichka'
aksi_username = 'aksi_maksi'


def prepare_message(profiles):
    text = "Hello bitches!!!\n" \
           "Сегодня {date}" \
        .format(
            date=date.today()
        )

    for profile in profiles:
        text += f"\n{profile['username']}: {profile['ranking']}"

    return text


def daily_informer():
    profiles = [get_profile(aksi_username), get_profile(sula_username)]
    text = prepare_message(profiles)
    send_message(text)


schedule.every().day.at("14:47").do(daily_informer)

while True:
    schedule.run_pending()
    time.sleep(1)
