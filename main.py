import time
import random
import schedule
import subprocess
import utils


def send_message():
    subprocess.call("osascript message.applescript '%s' '%s'" % (f'{utils.phone_number}', f'{random.choice(utils.message)}'), shell=True)


if __name__ == '__main__':
    schedule.every().day.at(utils.scheduled_time).do(send_message)

    while True:
        schedule.run_pending()
        time.sleep(1)
