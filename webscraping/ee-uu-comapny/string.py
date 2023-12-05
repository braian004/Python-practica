from bs4 import BeautifulSoup
import requests
import pandas as pd
# div class="fran-info"

url = 'https://www.visitingangels.com/senior-homecare-bend-oregon-97702_436'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
data = soup.find_all("div", class_="fran-info")

print(data)

# ation in the united states  location   bussines name   owner name   adsdress   CONTACTfrom bs4 import BeautifulSoup
