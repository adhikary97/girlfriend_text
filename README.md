# girlfriend_text
Send text to girlfriend (or really anyone with a phone number) in the morning

1. Configure your settings in `util.py`.
```py
phone_number = "phone number" # enter the target phone number inside quotation marks.  use the format "+15555555555"
message = "Good Morning Babe" # just make sure the message is inside quotation marks. An example is "Did you sleep well?"
scheduled_time = "08" # make sure the hour has 2 digits (24-hour standard).
```

Note that if you wish to send a message on a specific minute, you'll have to edit `main.py`.
If you want to send a message everyday at 8:45 AM, you will need to set `scheduled_time = "08:45"` in `util.py` and change line 8 of `main.py`
\t`hour = datetime.datetime.now().strftime('%H')` -> `hour = datetime.datetime.now().strftime('%H:%M')`

2. Run the script with `python3 main.py`.
