#!/usr/bin/env python3
import requests
import os
import json
from random import randint
from time import sleep
import random
import traceback
import time


def agent():
    agents = random.choice(open("useragent.txt", 'r').readlines()).replace("\n", "")
    return agents


useragent = {"User-Agent": agent()}  #{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
sleep_time2 = 30

#apigateway = "http://apigateway.domainanda:8080/getfile/"
#creds = open('creds.json')
#credentials = json.load(creds)

def region(domainn):
    re = requests.get(f"http://ip-server-kamu:33610/status/{domainn}").json()
    return re["status code"]

#print(result["status code"])

#def screenshot_page(copy_domain):
#    global datajpg
    #192.168.1.1 example ip
#    x = requests.get(f"http://apigateway.domainanda:8080/screenshot/{copy_domain}")
#    string = (x.text)
#    datajpg = (string[13:50])
    #print(x.text)
#    pass

def telegram_bot_sendtext_untuk_agungsurya(bot_message3):
   # bot_token = 'token-telegram-bot'
   # bot_chatID = 'chat-id-kamu'
    send_text_v2 = (f"http://localhost:8080/bot-telegram-codeigniter-dasboard/telegram.php?id={bot_message3}")
    #send_text_v2 = (f"http://api.domainanda/telegram.php?id={bot_message3}")  #'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message3 + '&disable_notification=true'
    result_v2 = requests.get(send_text_v2)
    #print(result_v2)

def telegram_bot_sendtext(bot_message):
    bot_token = 'token-telegram-bot' #credentials["bot-token"]
    bot_chatID = 'chat-id-kamu' #credentials["bot-chat-id"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=MarkdownV2&text=' + bot_message + '&disable_notification=true'
    result = requests.get(send_text)
    #print(result)

def telegram_bot_sendtext_v1(bot_message2):
    bot_token = 'token-telegram-bot' #credentials["bot-token"]
    bot_chatID =  'chat-id-kamu' #credentials["bot-chat-id"]
    send_text_v1 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message2 + '&disable_notification=true'
    result_v1 = requests.get(send_text_v1)
    #print(result_v1)

if (os.path.exists("monitor.json")):
    previous_monitor = open("monitor.json")
    domain_dict = json.load(previous_monitor)
else:
    domain_dict = {}

def check_status(url, param_timeout):
    global useragent
    useragent = {"User-Agent": agent()}
    copy_domain = url.replace("https://","")
    try:
        status_code = requests.get(url, timeout=param_timeout, headers=useragent).status_code
        #print(f"{status_code}{copy_domain}")
        if (status_code != 200):
            #screenshot_page(copy_domain)
            telegram_bot_sendtext_untuk_agungsurya(copy_domain)
            #telegram_bot_sendtext_v1(f"bot mendapatkan status code {status_code} ketika mengecek domain {copy_domain}. Pengecekan ulang akan dilakukan dalam {sleep_time2} detik mencoba mengambil screenshot web jika berhasi {apigateway}{datajpg}.jpg")
            sleep(sleep_time2)
            status_code = region(copy_domain)
     #       print(domain)
           # status_code = requests.get(url, timeout=param_timeout, headers=useragent).status_code
           # sleep(sleep_time2)
            
            if (status_code == 200):
                #print(f"{status_code}{copy_domain}")
                #telegram_bot_sendtext_v1(f"pengecekan berhasil status code adalah {status_code}")
                telegram_bot_sendtext_untuk_agungsurya(f"pengecekan code adalah{status_code}")
    except Exception as e:
        status_code = 0
        telegram_bot_sendtext(f"bot mengalami error ketika mengecek status code\nDetail Error:```\n{e}\n``` ")
        print(e)
    return status_code

def sanitize_input(domain):
    if ("http" not in domain):
        domain = "https://" + domain
    domain = domain.replace("\n", "")
    domain = domain.strip(" ")
    return domain


#domains = open("domain.txt", 'r').readlines()

def iterateDomains(domains, sleep_time=5, timeout=180):
    for domain in domains:
        copy_domain = domain
        domain = sanitize_input(domain)
        sleep(randint(1,sleep_time))
        status_code = check_status(domain, timeout)
        if (domain in domain_dict):
            if (domain_dict[domain] != status_code):
                status_changed = f"domain {copy_domain} status changed from previous {domain_dict[domain]} into {status_code}"
                telegram_bot_sendtext_v1(status_changed) # doesn't work ?
                print(status_changed)
        if (status_code == 200):
            message_status_code = (f"domain {copy_domain} is up")
            print(message_status_code)
        else:
            message_status_code_down = f"domain {copy_domain} is down, status code = {status_code}"
            telegram_bot_sendtext_v1(message_status_code_down) # this also doesn't work
            print(message_status_code_down)
        domain_dict[domain] = status_code

    json_f = json.dumps(domain_dict)
    json_file = open("monitor.json", "w")
    json_file.write(json_f)
    json_file.close()
while (True):
    try:
        domains = open("domain.txt", 'r').readlines()
        telegram_bot_sendtext_untuk_agungsurya("script mulai berjalan") #print ("script mulai berjalan")  #telegram_bot_sendtext_untuk_agungsurya("script mulai berjalan") #telegram_bot_sendtext("script mulai berjalan")
        start = time.time()
        iterateDomains(domains)
        end = time.time()
        time_required = round(end - start)
        telegram_bot_sendtext_untuk_agungsurya(f"script telah selesai berjalan, waktu berjalan:  {time_required} sekon") #print(f"script telah selesai berjalan, waktu berjalan:  {time_required} sekon")   #telegram_bot_sendtext_untuk_agungsurya(f"script telah selesai berjalan, waktu berjalan:  {time_required} sekon") #telegram_bot_sendtext(f"script telah selesai berjalan, waktu berjalan:  {time_required} sekon")
        print(f"program telah selesai dengan waktu {time_required} sekon")
    except Exception as e: 
        telegram_bot_sendtext_untuk_agungsurya(e)
