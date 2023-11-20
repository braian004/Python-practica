import requests
from bs4 import BeautifulSoup
import pandas as pd 
from lxml import etree
url = "https://listado.mercadolibre.com.ar/salud-equipamiento-medico/suplementos-alimenticios/proteina-whey_Desde_1_NoIndex_True"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Find all the <h2> elements with the specified class
rodilleras_titles = soup.find_all('h2', class_="ui-search-item__title")
rodilleras_precios = soup.find_all("span",class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript")
rodilleras_url = soup.find_all("a",class_="ui-search-item__group__element ui-search-link" )
# Function to extract the titles

def extract_data(html):
    clear = []
    for title in html:
        # Extract the text within the <h2> tags
        text = title.get_text()
        clear.append(text)
    return clear

# Call the function to extract the titles
rodilleras_url = soup.find_all("a",class_="ui-search-item__group__element ui-search-link" )
rodilleras_url = [i.get('href')for i in rodilleras_url]

cleaned_product_precios = extract_data(rodilleras_precios)
cleaned_product_titles = extract_data(rodilleras_titles)

# print(cleaned_product_titles)
lista_titulos = []
lista_precios = []
lista_urls=[]

siguiente = "https://listado.mercadolibre.com.ar/rodilleras-deportivas_Desde_1_NoIndex_True"
while True:
    r = requests.get(siguiente)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')

        rodilleras_titles = soup.find_all("h2",class_="ui-search-item__title")
        rodilleras_titles = [i.text for i in rodilleras_titles]
        lista_titulos.extend(rodilleras_titles)
        
        dom = etree.HTML(str(soup))
        rodilleras_urls = dom.xpath("//a[@class='ui-search-item__group__element ui-search-link']/@href")    
        lista_urls.extend(rodilleras_urls)
        
        rodilleras_precios = soup.find_all("span",class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript")
        rodilleras_precios = [i.text for i in rodilleras_precios] 
        lista_precios.extend(rodilleras_precios)

        ini = soup.find("li",class_="andes-pagination__button andes-pagination__button--current")
        ini= int(ini.text)

        can = soup.find("li",class_="andes-pagination__page-count")

        can = can.text
        can = int(can.replace("de ",""))

    else:
        break
    print(ini,can)    
    if ini == can:
        break

    dom = etree.HTML(str(soup))
    siguiente = dom.xpath("//li[@class='andes-pagination__button andes-pagination__button--next']/a")[0].get('href')   

df = pd.DataFrame({'titulo':lista_titulos,'precios':lista_precios,'url':lista_urls})
# df = df.reset_index(drop=True)
df.to_csv('webscraping/mercado-libre-rodillera/proteina-data.csv',index=False)#direccion para .py and ipynb just 'name.csv'

# df.to_csv('Rodilleras.csv', index=False)
