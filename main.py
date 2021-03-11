import datetime
import time as t
import re
import subprocess
import util


def send_message():
    pattern = r'08:\d{2}:\d{2}'
    while True:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        match = re.match(pattern, time)
        if match:
            subprocess.call(f"bash runner.bash '{util.phone_number}' '{util.message}'", shell=True)
            t.sleep(86400)


if __name__ == '__main__':
    send_message()
