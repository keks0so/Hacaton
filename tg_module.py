import requests
import json




with open("tg_creds.json", 'r') as json_file:
    tg_creds = json.load(json_file)

bot_id = tg_creds["bot_token"]
chat_id = tg_creds["chat_id"]


def send_emergency_message(what, where):
        
    telegram_api_url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id=-{chat_id}&text={what}, произошло {where}"
    tel_resp = requests.get(telegram_api_url)
    if tel_resp.status_code == 200:
        print("Message was send")
    else:
        print("smth went wrong")
