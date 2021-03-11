import datetime
import subprocess
import util


def send_message():
    while True:
        hour = datetime.datetime.now().strftime('%H')
        if hour == util.scheduled_time:
            subprocess.call(f"bash runner.bash '{util.phone_number}' '{util.message}'", shell=True)
            time.sleep(86400)


if __name__ == '__main__':
    send_message()
