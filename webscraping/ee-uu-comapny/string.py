from bs4 import BeautifulSoup
import requests
import pandas as pd
# div class="fran-info"

# url = 'https://www.visitingangels.com/senior-homecare-bend-oregon-97702_436'
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'lxml')
# data = soup.find_all("div", class_="fran-info")
# # print(data)
# data_order = data.split("><") 
# for i in data_order:
#     print(i)
# print(data_order)
# ation in the united states  location   bussines name   owner name   adsdress   CONTACTfrom bs4 import BeautifulSoup
# data = ['<div class="fran-info">Visiting Angels<br/>376 SW Bluff Dr #9 <br/>Bend OR 97702<br/>541-617-3868</div>']
# location = []
# bussines_name = []
# address = []
# Conatact = []
# for i in data :
    
#     print(i)
import re

data = ['<div class="fran-info">Visiting Angels<br/>376 SW Bluff Dr #9 <br/>Bend OR 97702<br/>541-617-3868</div>']

location = []
business_name = []
address = []
contact = []

for i in data:
    # Extraer solo el texto
    clean_text = re.sub('<[^<]+?>', '', i).strip()

