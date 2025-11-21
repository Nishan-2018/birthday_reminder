import json
import datetime
import notifier
import os

DATA_FILE = "birthdays.json"
# You should change this to a unique topic for your own privacy
NTFY_TOPIC = "birthday_wish_nishan_unique_123" 

def load_birthdays():
    """Loads birthday data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def check_birthdays():
    """Checks if today matches any birthday."""
    birthdays = load_birthdays()
    # Use IST timezone (UTC+5:30) to ensure we check the correct "today"
    # even if the server is in UTC.
    tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    today = datetime.datetime.now(tz).date()
    today_str = today.strftime("%m-%d")
    
    print(f"Checking birthdays for {today_str}...")
    
    found = False
    for person in birthdays:
        if person['date'] == today_str:
            notifier.notify(person['name'], topic=NTFY_TOPIC)
            found = True
            
    if not found:
        print("No birthdays today.")

if __name__ == "__main__":
    check_birthdays()
