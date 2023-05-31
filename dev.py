#3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    elements = soup.find_all({"class": "example-class"})
    if elements:
        elements_name = elements.text.strip()
        print(elements_name)
    else:
        print("Таких елементів немає на сторінці")