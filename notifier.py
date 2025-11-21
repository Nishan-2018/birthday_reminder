import os
import requests
import platform

import subprocess

def send_desktop_notification(title, message):
    """Sends a desktop notification on macOS."""
    if platform.system() == 'Darwin':
        script = f'display notification "{message}" with title "{title}"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to send desktop notification: {e}")
    else:
        print(f"Desktop Notification: {title} - {message}")

def send_iphone_notification(topic, title, message):
    """Sends a notification to iPhone via ntfy.sh."""
    try:
        requests.post(
            f"https://ntfy.sh/{topic}",
            data=message.encode(encoding='utf-8'),
            headers={
                "Title": title,
            }
        )
        print(f"Sent iPhone notification to topic: {topic}")
    except Exception as e:
        print(f"Failed to send iPhone notification: {e}")

def notify(name, topic="birthday_wisher_test"):
    """Orchestrates the notification process."""
    title = "Birthday Wisher"
    message = f"Today is {name}'s birthday! Don't forget to wish them."
    
    print(f"Sending wish for {name}...")
    send_desktop_notification(title, message)
    send_iphone_notification(topic, title, message)
