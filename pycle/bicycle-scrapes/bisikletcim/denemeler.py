import os
import wget
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


url = 'https://www.bisikletcim.com/carraro-cr-race-022-28-jant-bisiklet'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

parsed = BeautifulSoup(webpage, 'html.parser')

# properties = parsed.find(attrs={'class':' tb-proerties'})

print(parsed)