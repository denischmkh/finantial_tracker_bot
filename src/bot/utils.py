from datetime import datetime
import pytz

def get_kiev_time():
    kiev_tz = pytz.timezone("Europe/Kiev")
    return datetime.now(kiev_tz)

