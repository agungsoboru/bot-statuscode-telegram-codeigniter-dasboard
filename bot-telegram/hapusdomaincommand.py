#import os
#from telegram.ext import Updater, CommandHandler
import os
from telegram.ext import Updater, CommandHandler
import requests
from telegram import InputFile
import subprocess

print("Ready!")

#import os
#from telegram.ext import Updater, CommandHandler

def hapus_domain(update, context):
    domain = update.message.text.split(" ")[1]
    domain_found = False
    with open("domain.txt", "r") as f:
        domains = f.readlines()
    with open("domain.txt", "w") as f:
        for d in domains:
            if d.strip() != domain:
                f.write(d)
            else:
                domain_found = True
    if domain_found:
        update.message.reply_text(f"Domain {domain} berhasil dihapus dari file.")
    else:
        update.message.reply_text(f"Domain {domain} tidak ditemukan dalam file.")


def hapus_domain2(update, context):
    domain = update.message.text.split(" ")[1]
    domain_found = False
    with open("domain2.txt", "r") as f:
        domains = f.readlines()
    with open("domain2.txt", "w") as f:
        for d in domains:
            if d.strip() != domain:
                f.write(d)
            else:
                domain_found = True
    if domain_found:
        update.message.reply_text(f"Domain {domain} berhasil dihapus dari file.")
    else:
        update.message.reply_text(f"Domain {domain} tidak ditemukan dalam file.")



def status_api(update, context):
    respond = requests.get(f"http://api.domainanda:11119/api")
    status_code2 = requests.get(f"http://ip-server-kamu:33610/api/")
    #print(respond.text)
    send = (f"status api server 1 = {respond.text} status api server 2 = {status_code2.text}")
    
    update.message.reply_text(f"{send}")



def list_domain(update, context):
    chat_id = update.message.chat_id
    file_name = "domain.txt"
    file_name2 = "domain2.txt"
    if chat_id == chat-id-kamu:

        if os.path.exists(file_name):
            with open(file_name, "rb") as f:
                update.message.reply_document(document=InputFile(f), filename=file_name)
                if os.path.exists(file_name2):
                    with open(file_name2, "rb") as a:
                        update.message.reply_document(document=InputFile(a), filename=file_name2)
    else:
        update.message.reply_text("You are not authorized to use this function. This action will be reported.")
        print(update) 




def cek(update, context2):
    message = update.message.text.split(" ")[1]
    status_code = requests.get(f"https://{message}")
    update.message.reply_text(f"status code {message} {status_code}")


def shell(update, context):
    chat_id = update.message.chat_id
    message = update.message.text.split(" ")[1]
    if chat_id == chat-id-kamu:
        output = subprocess.run(message, capture_output=True)
        update.message.reply_text(output.stdout.decode())

    else:
        update.message.reply_text("You are not authorized to use this function. This action will be reported.")


token = "token-telegram-bot"

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

hapus_domain_handler = CommandHandler("hapusdomain", hapus_domain)
hapus_domain_handler2 = CommandHandler( "hapusdomain2", hapus_domain2)
statusapi = CommandHandler( "status_api", status_api)
listdomain = CommandHandler( "list_domain", list_domain)
ceks = CommandHandler( "cek", cek)
shells = CommandHandler( "shell", shell)


dispatcher.add_handler(hapus_domain_handler)
dispatcher.add_handler(hapus_domain_handler2)
dispatcher.add_handler(statusapi)
dispatcher.add_handler(listdomain)
dispatcher.add_handler(ceks)
dispatcher.add_handler(shells)


updater.start_polling()
updater.idle()



