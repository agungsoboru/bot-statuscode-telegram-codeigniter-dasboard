import random
from random import randint
import json
import requests
from urllib.parse import quote
import os
import re
from time import sleep
# find a random user agent from useragent.txt 
agent = lambda : random.choice(open("useragent.txt", "r").readlines()).replace("\n", "")

with open("credentials.json") as j_file:
    creds = json.load(j_file)
with open("domain.txt", "r") as domain:
    domains = domain.readlines()
if (os.path.exists("monitor.json")):
    with open("monitor.json") as monitor:
        domain_dict = json.load(monitor)
else:
    domain_dict = {}
def telegram_sendtext(message, version=1, disable_notification=True):
    if (version < 0 or version > 2): 
        raise ValueError("Choose either version 1 or 2")
    bot_token = creds["telegram"]["bot-token"]
    bot_chat_id = creds["telegram"]["bot-chat-id"]    
    if (version == 1):
        text_format = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={message}"
    else:
        text_format = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=MarkdownV2&text={message}"
    if (disable_notification):
        text_format += "&disable_notification=true"
    else:
        text_format += "&disable_notification=false"
    try:
        requests.get(text_format)
    except requests.exceptions.ConnectionError:
        print("Site is unreachable due to Connection Error")
    return

def formatGivenUrl(domain):
    # if http or https not in domain, then a regular expression match will happen.
    if not re.match("(?:http|https)://", domain):
        return "https://" + domain.replace("\n","")
    return domain

def formatMessageForTelegram(domain, status_code, error=False, error_message=None):
    if (not error):
        message = f"Domain `{domain}` is down,\nstatus code is {status_code}"
    else:
        message = f"The bot had an error when checking the status code for domain `{domain}`\nError Details:```{error_message}```"
    return quote(message)

def check_status(domain, timeout, sleep_time):
    useragent = {"User-Agent": agent()}
    try:
        status_code = requests.get(formatGivenUrl(domain), timeout=timeout, headers=useragent).status_code
        if (status_code != 200):
            telegram_sendtext(formatMessageForTelegram(domain, status_code))
            # will implement region based checking later
            # status_code = region(domain)
            print("domain down", domain, status_code)
    except Exception as e:
        status_code = 0
        telegram_sendtext(telegram_sendtext(formatMessageForTelegram(domain, status_code, error=True, error_message=e)), version=2)
        print(e)
    return status_code

def iterate_domains(domains, sleep_time=5, timeout=180):
    for domain in domains:
        url = formatGivenUrl(domain)
        sleep(randint(1, sleep_time))
        status_code = check_status(url, timeout, sleep_time)
        if (domain in domain_dict):
            if (domain_dict[domain] != status_code):
                status_changed = f"Domain {domain} status changed from previous {domain_dict[domain]} into {status_code}"
                telegram_sendtext(status_changed)
                print(status_changed)
        if (status_code == 200):
            status_up = f"Domain {domain} is up"
            print(status_up)
        domain_dict[domain] = status_code
    json_object = json.dumps(domain_dict)
    with open("monitor.json", "w") as monitor:
        monitor.write(json_object)

iterate_domains(domains)