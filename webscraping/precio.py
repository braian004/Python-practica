'''webscraping precio'''
import requests
from bs4 import BeautifulSoup

def get_price(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "html.parser")  # Use "html.parser" here
    price_with_eur = soup.find("span", class_="andes-money-amount__fraction").text
    return price_with_eur

while True:
    url = input("¿URL del producto para saber el precio?")
    if url == "":
        break
    print(get_price(url))