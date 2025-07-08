# check_sites.py - script to automatically check sites for updated articles

import requests
from datetime import datetime

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
    return status

def main():
    print(f"Internet check run at {datetime.utcnow()} UTC")
    for site in SITES:
        status = check_site(site)
        print(f"{site} --> {status}")

if __name__ == "__main__":
    main()
