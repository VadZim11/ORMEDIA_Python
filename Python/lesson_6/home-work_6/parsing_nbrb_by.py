import requests
from bs4 import BeautifulSoup
import ast

def get_html(url):
    r = requests.get(url)
    return r.text
        
def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.find("body").text
    return h1

def main():
    url = "https://nbrb.by/API/ExRates/Rates?Periodicity=0"
    list_cur = ast.literal_eval((get_data(get_html(url))))

    # print(list_cur[0])
    # print(type(list_cur[0]))

    for i in range(len(list_cur)) :
        # if str(list_cur[i]["Cur_Abbreviation"]) == "USD" or str(list_cur[i]["Cur_Abbreviation"]) == "RUB" or str(list_cur[i]["Cur_Abbreviation"]) == "EUR" :
            print(str(list_cur[i]["Date"])[0:10] + " rate 1 " 
            + str(list_cur[i]["Cur_Abbreviation"])
            + " - " +  str(list_cur[i]["Cur_OfficialRate"]) 
            + " BIN")

if __name__ == "__main__":
    main()