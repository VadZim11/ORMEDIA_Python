import requests

def get_money(text):
    s = text.split()

    if len(s)>1:
        url = f"http://www.nbrb.by/API/ExRates/Rates/{s[1]}?ParamMode=2"
        r = requests.get(url).json()

        data = ("- " + str(r["Date"])[0:10] + " rate " 
            + str(r["Cur_Name"]) + " "
            + str(r["Cur_Scale"]) + " "
            + str(r["Cur_Abbreviation"])
            + " - " +  str(r["Cur_OfficialRate"]) 
            + " BIN")
        return data
        
    else:
        url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
        r = requests.get(url).json()
        data = ""
        for i in range(len(r)) :
            data += ("- " + str(r[i]["Date"])[0:10] + " rate " 
            + str(r[i]["Cur_Name"]) + " "
            + str(r[i]["Cur_Scale"]) + " "
            + str(r[i]["Cur_Abbreviation"])
            + " - " +  str(r[i]["Cur_OfficialRate"]) 
            + " BIN\n")
        return data

def main():
    print(get_money("курс"))

if __name__ == "__main__":
    main()