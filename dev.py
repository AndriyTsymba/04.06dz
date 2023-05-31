#2
import requests
from bs4 import BeautifulSoup
response = requests.get("https://uk.wikipedia.org/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    tablee = soup.find_all("table")
    for i in tablee:
        print(i)