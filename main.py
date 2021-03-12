import datetime
import subprocess
import utils


def send_message():
    while True:
        hour = datetime.datetime.now().strftime('%H')
        if hour == utils.scheduled_time:
            subprocess.call(f"bash runner.bash '{utils.phone_number}' '{utils.message}'", shell=True)
            time.sleep(86400)


if __name__ == '__main__':
    send_message()
