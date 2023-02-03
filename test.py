import requests
from bs4 import BeautifulSoup
import csv
import os.path
import json 


default_addr = "https://www.mechta.kz/product/telefon-sotovyy-apple-iphone-11-64gb-black-eco/"
url = default_addr[30:]
print(url)
headers = {'Content-type': 'application/json'}
page_json = requests.post(default_addr, headers=headers)
page = requests.get(default_addr)
market_data = page.json()
print(market_data)