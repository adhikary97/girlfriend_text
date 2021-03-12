# Girlfriend Text
Send text to girlfriend (or really anyone with a phone number) in the morning

## 1. Configure your settings in `utils.py`.
```py
phone_number = "phone number" # enter the target phone number inside quotation marks. use the format "+15555555555"
message = ["Good Morning Babe", "Good morning my love", "Good morning cutie"] # just make sure the message is inside quotation marks. An example is "Did you sleep well?"
scheduled_time = "08:00" # make sure the hour has 2 digits (24-hour standard).
```

Note: If you want to send a message everyday at 8:45 AM, you will need to set `scheduled_time = "08:45"` in `utils.py`

## 2. Install requirements: `pip install -r requirements.txt`

## 3. Run the script with: `python3 main.py`
