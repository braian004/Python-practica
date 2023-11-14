from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.resultados-futbol.com/primera"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")

#equipos
eq = soup.find_all('td', class_="equipo")
# print(eq)

# Limpia etiquetas
count = 0
equipos = list()
for i in eq:
    if count < 20 :
        equipos.append(i.text)
    else:
        break
    count+=1
# print(equipos)    

#puntos
p = soup.find_all('td',class_="pts")
# print(p)

count = 0
puntos = list()
for i in p:
    if count < 20 :
        puntos.append(i.text)
    else:
        break
    count+=1

#ordenamos de mayor a menor
s = sorted(puntos,key=lambda x: int(x),reverse=True)  
# print(s
# print(len(puntos))

sd = pd.DataFrame({'Equipos':equipos,'Puntos':s},index=list(range(1,21)))

# print(sd)

sd.to_csv('webscraping/errodring/equipo.csv', index=False)# csv 

# Ruta del archivo Excel
excel_file = 'webscraping/errodring/equipo.xlsx'
# Guardar el DataFrame en un archivo Excel.
sd.to_excel(excel_file, index=False)
