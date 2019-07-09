import requests
from token import token

URL = "https://api.telegram.org/bot" + str(token) + "/"

def get_updete(html):
    url + URL + "getupdates"
    r = requests.get(url)
    print(r)

def main():
    get_updete()

if __name__ == "__main__":
    main()