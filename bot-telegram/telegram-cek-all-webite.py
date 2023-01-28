from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import json
import requests




def telegram_bot_sendtext(bot_message):
    bot_token = 'token-telegram-bot' #credentials["bot-token"]
    bot_chatID = 'chat-id-kamu' #credentials["bot-chat-id"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=MarkdownV2&text=' + bot_message + '&disable_notification=true'
    result = requests.get(send_text)

def telegram_bot_sendtext_v1(bot_message2):
    bot_token = 'token-telegram-bot' #credentials["bot-token"]
    bot_chatID =  'chat-id-kamu' #credentials["bot-chat-id"]
    send_text_v1 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message2 + '&disable_notification=true'
    result_v1 = requests.get(send_text_v1)
    #print(result_v1)



'''
work wokr workwrokworkworkwrokworkworkworkwor
okrowkrowkrowkrowkrowkrowkrowkrow
orwkrowkowkrowko

'''
def check_domain(domain):

    try:

        
        
        #return domains
        
        # Kirim request ke domain
        response = requests.get(domain)
        # Cek apakah status code valid
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Jika terjadi error, cetak pesan error
        print(f"Error: {e}")
        telegram_bot_sendtext(f"bot mengalami error ketika mengecek status code\nDetail Error:```\n{e}\n``` ")
    else:
        # Cetak hasil request
        print(f"Domain: {domain}, Status Code: {response.status_code}")
        telegram_bot_sendtext_v1(f"Domain: {domain}, Status Code: {response.status_code}")
        



def load_json_file(filename):
    try:
        # Buka file JSON
        file = open(filename, "r")
        # Muat data JSON
        data = json.load(file)
    except Exception as e:
        # Jika terjadi error, kembalikan None
        return None
    else:
        # Kembalikan data JSON
        return data
    finally:
        # Tutup file
        file.close()

# Muat file JSON


# if data is None:
#     # Jika terjadi error, cetak pesan error
#     print("Error: Gagal memuat file JSON")
# else:
#     # Cetak data JSON
#     print(data)








# Muat data JSON

#data = json.loads('{"https://google.com": 200, "https://yahoo.com": 0, "https://youtube.com":500}')

# Cari domain yang status code-nya 0 atau 500



def start(update, context):
    # Buat tombol dengan perintah /start main
    button = InlineKeyboardButton("Cek ulang semua", callback_data="/start")
    # Buat keyboard dengan satu tombol
    keyboard = [[button]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Kirim pesan dengan tombol
    update.message.reply_text("Silakan klik tombol untuk memulai cek ulang semua!", reply_markup=reply_markup)

updater = Updater("token-telegram-bot", use_context=True)
dispatcher = updater.dispatcher

# Tambahkan handler untuk perintah /start
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# Tambahkan handler untuk menangani tombol yang diklik
def button(update, context):
    query = update.callback_query
    print ("tes")
    data = load_json_file("monitor.json")
    #jsonload()
    domains = [domain for domain, status_code in data.items() if status_code in (0, 500)]
    for domain in domains:
        check_domain(domain)

    # Jalankan perintah yang ditentukan di tombol
    #update.message.reply_text("Anda telah memulai main!")

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

updater.start_polling()
