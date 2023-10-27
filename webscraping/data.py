import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://listado.mercadolibre.com.ar/rodilleras-deportivas#D[A:rodilleras%20deportivas]"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Find all the <h2> elements with the specified class
rodilleras_titles = soup.find_all('h2', class_="ui-search-item__title")

# Function to extract the titles
def extract_titles(html_titles):
    cleaned_titles = []
    for title in html_titles:
        # Extract the text within the <h2> tags
        title_text = title.get_text()
        cleaned_titles.append(title_text)
    return cleaned_titles

# Call the function to extract the titles
cleaned_product_titles = extract_titles(rodilleras_titles)

# Print the cleaned product titles
for title in cleaned_product_titles:
    print(title)

rodilleras_precio = soup.find_all("span",class_="andes-money-amount__fraction")

# Function to extract the titles
def extract_titles_precio(html_titles):
    cleaned_titles = []
    for title in html_titles:
        # Extract the text within the <h2> tags
        title_text = title.get_text()
        cleaned_titles.append(title_text)
    return cleaned_titles

# Call the function to extract the titles
cleaned_product_titles = extract_titles_precio(rodilleras_precio)

# Print the cleaned product titles
for title_precio in cleaned_product_titles:
    print(title_precio)

sd = pd.DataFrame('Equipos':title_precio,'Puntos':title,index=list())
print(sd)