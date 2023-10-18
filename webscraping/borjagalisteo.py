import requests
from bs4 import BeautifulSoup

def get_price(url):
    html_text = requests.get(url).text
    soup= BeautifulSoup(html_text,"html_perser") 
    price_with_eur = soup.find("span",{"class":"andes-money-amount__fraction"}).contents[0]
    # <span class="andes-money-amount__fraction" aria-hidden="true">12.848</span>
    return price_with_eur
while True:
    url = input("¿url del prodructo para saber el precio?")
    if url == "":
        break
    print(get_price(url))