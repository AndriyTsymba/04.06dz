#4
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.example.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    h1 = soup.find_all("h1").text
    print(h1)
else:
    print("No connection or no h1")