import requests
import json
from my_token import TOKEN

URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates():
    url = f"{URL}/getupdates"
    r = requests.get(url)
    #print(r.json())
    return r.json()

def get_message():
    data = get_updates()
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_id = data["result"][-1]["message"]["message_id"]
    message_text = data["result"][-1]["message"]["text"]

    message ={"chat_id": chat_id, "text": message_text, "message_id": message_id}

    print(message)

    return message

def send_message(chat_id, text):
    url =f"{URL}/sendmessage?chat_id={chat_id}&text={text}"#.format(, , )
    print(url)
    requests.get(url)

def get_money():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    r = requests.get(url)
    return r.json()

def main():
    money = get_money() 
    #curs_money = ""   

    for i in range(len(money)):
        if str(money[i]["Cur_Abbreviation"]) == "EUR":
            curs_money = ("- " + str(money[i]["Date"])[0:10] 
                + " rate " + str(money[i]["Cur_Name"]) + " " 
                + str(money[i]["Cur_Scale"]) + " " 
                + str(money[i]["Cur_Abbreviation"]) + " - "
                +  str(money[i]["Cur_OfficialRate"]) + " BIN")

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