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
    #d = get_updates()
    #m = get_money()
    #et_message()

    #with open("updates.json", "w") as file:
     #  json.dump(d, file, indent=2, ensure_ascii=False)

    #with open("money.json", "w") as file:
     #  json.dump(m, file, indent=2, ensure_ascii=False)

    #print(get_message())
    money = get_money() 
    curs_money = ""   

    for i in range(len(money) -1):
        curs_money += "- " + str(money[i]["Date"])[0:10] + " rate " + str(money[i]["Cur_Name"]) + " " + str(money[i]["Cur_Scale"]) + " " + str(money[i]["Cur_Abbreviation"]) + " - " +  str(money[i]["Cur_OfficialRate"]) + " BIN\n"

    curs_money += "- " + str(money[-1]["Date"])[0:10] + " rate " + str(money[-1]["Cur_Name"]) + " " + str(money[-1]["Cur_Scale"]) + " " + str(money[-1]["Cur_Abbreviation"]) + " - " +  str(money[-1]["Cur_OfficialRate"]) + " BIN"
    print(curs_money)
    answer = get_message()
    chat_id = answer["chat_id"]
    text = answer["text"]

    if "ничего" in text:
        send_message(chat_id, "Тогда покедово))")

    if "курс" in text:
        send_message(chat_id, curs_money)    

if __name__ == "__main__":
    main()