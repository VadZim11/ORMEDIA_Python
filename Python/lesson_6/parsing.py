import request
from bs4 import BeautifulSoup

def get_html(url):
    r = request.get(url)
    return r.text
        
def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.find("div", id="home-welcome").find("header").find("h1").text
    return h1

def main():
    url = "https://worldpress.org/"
    print(get_data(get_html(url)))





if __name__ == "__main__":
    main()
