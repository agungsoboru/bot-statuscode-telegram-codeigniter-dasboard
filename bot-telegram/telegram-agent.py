from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
import requests
import re


def telegram_bot_sendtext(bot_message):
    bot_token = 'token-telegram-bot' #credentials["bot-token"]
    bot_chatID = chat-id-kamu #'chat-id-kamu' #credentials["bot-chat-id"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=MarkdownV2&text=' + bot_message + '&disable_notification=true'
    result = requests.get(send_text)

def telegram_bot_sendtext_v1(bot_message2):
    bot_token = 'token-telegram-bot' #credentials["bot-token"]
    bot_chatID =  chat-id-kamu#'chat-id-kamu' #credentials["bot-chat-id"]
    send_text_v1 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message2 + '&disable_notification=true'
    result_v1 = requests.get(send_text_v1)
    #print(result_v1)

updater = Updater("token-telegram-bot",
                  use_context=True)

dispatcher: Dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    #global update
    #global bot

    bot: Bot = context.bot
    #bot.send_message(chat_id=update.effective_chat.id, text="You have just entered start command")
    #bot.send_message(chat_id=update.effective_chat.id, text="You have just entered start command")

    #requests.get(f"https://{domain}").status_code}
    text = update.message.text
    regex = r"([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

# mencari semua pola yang cocok dengan regex
    domains = re.findall(regex, text)

# menggabungkan semua elemen list menjadi string dengan menggunakan spasi sebagai pemisah
    domains_string = " ".join(domains)
#    return domains_string
    data_domain = str(domains_string)
    

    
    print (data_domain)
    my_function(data_domain)
    


def my_function(domains_string):
    

    while (True):
        try:
        
            x = requests.get(f"https://{domains_string}").status_code
            data =  str(x)
            telegram_bot_sendtext_v1(f"status {domains_string} {data} ")
            print (x)
            
            #bot.send_message(chat_id=update.effective_chat.id, text="You have just entered start command")
        
        except Exception as e:
            #telegram_bot_sendtext_v1(e)
            telegram_bot_sendtext(f"bot mengalami error ketika mengecek status code\nDetail Error:```\n{e}\n``` ")
            print(e)
        else:
            break
    
            

    #print(domains_string)
   # print (update.message.text)


dispatcher.add_handler(
 
    CommandHandler("cek", start))
    

updater.start_polling()



