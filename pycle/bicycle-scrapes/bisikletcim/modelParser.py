from bs4 import BeautifulSoup
import os

fileList = os.listdir('models/')

for i in fileList:
    openHtml = open('models/i')
    parsed = BeautifulSoup(openHtml, 'html.parser')
    properties = parsed.find(attr={'class':'tb-properties'})
    