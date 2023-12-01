from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# # div class="fran-info"
# # url = 'https://www.visitingangels.com/senior-homecare-bend-oregon-97702_436'

# def ext_data (url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     data = soup.find("div", class_="fran-info")
#     return data

#     # r = requests.get(url)
#     # soup = BeautifulSoup(r.content, 'lxml')
#     # data = soup.find("div", class_="fran-info")
# data_print= ext_data('https://www.visitingangels.com/senior-homecare-bend-oregon-97702_436')
# print(data_print)

# df = pd.DataFrame(data_print('location','busines name','address','cantact'))
# df

# location in the united states  location   bussines name   owner name   adsdress   CONTACTfrom bs4 import BeautifulSoup
import requests
import pandas as pd

def ext_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find("div", class_="fran-info")
    return data

url = 'https://www.visitingangels.com/senior-homecare-bend-oregon-97702_436'
data_tag = ext_data(url)

# Extracting specific information from the data_tag
location = data_tag.find('span', {'itemprop': 'addressLocality'}).text
business_name = data_tag.find('h1', {'class': 'location-title'}).text.strip()
address = data_tag.find('span', {'itemprop': 'streetAddress'}).text
contact = data_tag.find('span', {'itemprop': 'telephone'}).text

# Creating a DataFrame
data_dict = {
    'Location': [location],
    'Business Name': [business_name],
    'Address': [address],
    'Contact': [contact]
}

df = pd.DataFrame(data_dict)
print(df)
