'''FOR IMAGEN'''
import requests
from bs4 import BeautifulSoup

def save_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {filename}")
    else:
        print("Failed to download the image")

def get_image(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "html.parser")  # Use "html.parser" here
    img_element = soup.find("div", class_="x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy x1ypdohk")
    
    if img_element:
        img_src = img_element.get("src")
        return img_src
    else:
        return "Image not found on the page."

while True:
    url = input("¿URL del producto para download img?")
    if url == "":
        break
    image_url = get_image(url)
    
    if image_url != "Image not found on the page.":
        filename = input("Nombre de archivo para guardar la imagen: ")
        save_image(image_url, filename)
    else:
        print("Image not found on the page.")
    # print(get_price(url))