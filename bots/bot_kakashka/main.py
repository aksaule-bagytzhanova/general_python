import time
from datetime import date, datetime

import schedule

from bots.bot_kakashka.leetcode_parser import get_profile
from bots.bot_kakashka.telegram_sender import send_message

sula_username = 'desalichka'
aksi_username = 'aksi_maksi'


def prepare_message(profiles):
    text = "Hello bitches!!!\n" \
           "Сегодня {datetime}\n" \
        .format(
            datetime=time.strftime("%a, %d %b %Y %H:%M:%S")
        )

    for profile in profiles:
        text += f"\n{profile['username']}" \
                f"\nPoints   💲: {profile['points']}" \
                f"\nRealname   🛸: {profile['realName']}"  \
                f"\nTotal   🌠: {profile['total']}"   \
                f"\nEasy   🔨: {profile['easy']}"\
                f"\nMedium   ⚒: {profile['medium']}"\
                f"\nHard   ⚔️: {profile['hard']}" \
                "\n🚎️🚌️🚎️🚌️🚎️🚌️🚎️🚌️🚎️🚌️🚎️🚌️🚎️🚌️🚎️🚌️" \
                "\n"


    return text


def daily_informer():
    profiles = [get_profile(aksi_username), get_profile(sula_username)]
    text = prepare_message(profiles)
    send_message(text)


schedule.every().day.at("01:55").do(daily_informer)
# schedule.every().day.at("12:00").do(daily_informer)
# schedule.every().day.at("17:00").do(daily_informer)
# schedule.every().day.at("21:00").do(daily_informer)
# schedule.every().day.at("23:00").do(daily_informer)
while True:
    schedule.run_pending()
    time.sleep(1)
