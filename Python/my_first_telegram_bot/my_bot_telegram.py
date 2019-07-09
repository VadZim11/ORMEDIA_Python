import requests
from my_token import token

URL = "https://api.telegram.org/bot" + str(token) + "/"

def get_updates():
    url = URL + "getupdates"
    r = requests.get(url)
    print(r)

def main():
    get_updates()

if __name__ == "__main__":
    main()