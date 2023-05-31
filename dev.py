#1
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    h2 = soup.find_all("h2").text
    print(h2)
else:
    print("No connection or no h2")