# check_sites.py - script to automatically check sites for updated articles

import requests
from datetime import datetime
import os

SITES = [
    "https://scholar.google.com/",
    "https://arxiv.org/",
]

def check_site(url):
    try:
        response = requests.get(url, timeout=10)
        status = f"{response.status_code} {response.reason}"
    except requests.RequestException as e:
        status = f"ERROR: {e}"
    return f"{url} --> {status}"

def send_discord_message(message):
    webhook_url = os.environ["DISCORD_WEBHOOK"]
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    print(f"Discord response: {response.status_code}")

def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    results = [check_site(site) for site in SITES]
    message = f"🌐 **Internet Check @ {timestamp}**\n" + "\n".join(results)
    print(message)
    send_discord_message(message)

if __name__ == "__main__":
    main()
