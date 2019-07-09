import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text
        
def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.findAll("h2", {"class": "post__title"})
    list_name = set()
    for i in h1:        
        a = i.find("a").text
        list_name.add(a) 
    return list_name

def get_page(html):
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.find("a", {"class": "toggle-menu__item-link toggle-menu__item-link_pagination toggle-menu__item-link_bordered"}).get("href")
    return h1

def main():

    url = "https://habr.com/top/monthly/"
    finish_page = int(get_page(get_html(url))[-3:-1])

    # print(finish_page)

    list_articles_habr = list()

    for i in range(1, finish_page) :
        url = "https://habr.com/top/monthly//page" + str(i) + "/"
        list_articles_habr = list_articles_habr + list(get_data(get_html(url)))
    
    list_articles_habr.sort()
    print("За месяц вышло " + str(len(list_articles_habr)) + " статей: ")

    for i in range(len(list_articles_habr)):
        print("- " + str(list_articles_habr[i]))

if __name__ == "__main__":
    main()