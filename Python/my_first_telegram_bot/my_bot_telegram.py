import requests
import json
from my_token import token

URL = "https://api.telegram.org/bot" + str(token) + "/"

def get_updates():
    url = URL + "getupdates"
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_text = data["result"][-1]["message"]["text"]

    message ={"chat_id": chat_id, "text": message_text}

    return message

def send_message(chat_id, text):
     url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
     print(url)
     requests.get(url)

def get_money():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    r = requests.get(url)
    return r.json()


def main():    
    
    money = get_money() 
    curs_money = ""   

    for i in range(len(money)):
        curs_money += "- " + str(money[i]["Date"])[0:10] + " rate " + str(money[i]["Cur_Name"]) + " " + str(money[i]["Cur_Scale"]) + " " + str(money[i]["Cur_Abbreviation"]) + " - " +  str(money[i]["Cur_OfficialRate"]) + " BIN\n"

    answer = get_message()
    chat_id = answer["chat_id"]
    text = answer["text"]

    answers = {"ничего":"ничего", "курс":curs_money, "привет":"привет"}

    if text in answers:
        send_message(chat_id, answers[text])
    else:
        send_message(chat_id, "Извини такого запроса я не знаю(")  

if __name__ == "__main__":
    main()