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
# for title in cleaned_product_titles:
#     print(title)

#PRECIO

# Find all the <h2> elements with the specified class
rodilleras_precio = soup.find_all('span', class_="andes-money-amount__fraction")
# Function to extract the titles
def extract_precio(html_precio):
    cleaned_precio = []
    for precio in html_precio:
        # Extract the text within the <h2> tags
        precio_text = precio.get_text()
        cleaned_precio.append(precio_text)
    return cleaned_precio

# Call the function to extract the titles
cleaned_product_precio = extract_precio(rodilleras_precio)

# Print the cleaned product titles
# for title_precio in cleaned_product_titles:
#     print(title_precio)

rodilleras_precio_oferta = soup.find_all('div', class_="ui-search-coupon__label label-text-desktop")
rodilleras_precio_oferta = soup.find_all('span', class_="ui-search-price__discount")
# Function to extract the titles
def extract_precio_oferta(html_precio_oferta):
    cleaned_precio_oferta = []
    for precio_oferta in html_precio_oferta:
        # Extract the text within the <h2> tags
        precio_text = precio_oferta.get_text()
        cleaned_precio_oferta.append(precio_text)
    return cleaned_precio_oferta

# Call the function to extract the titles
cleaned_product_precio_oferta = extract_precio_oferta(rodilleras_precio_oferta)

# for precio_oferta in cleaned_product_precio_oferta:
#     print(precio_oferta)
 
df = pd.DataFrame(list(zip(cleaned_product_titles,cleaned_product_precio,cleaned_product_precio_oferta)), 
                  columns =['Titulo','Precio','Ofertas'])
df = df.reset_index(drop=True)
df.to_csv('Rodilleras.csv', index=False)