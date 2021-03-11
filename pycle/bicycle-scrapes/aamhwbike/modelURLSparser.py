import os
import wget
from bs4 import BeautifulSoup


bicycles = []

fileList = os.listdir("listPages/")
for file in fileList:
 
    parsed = BeautifulSoup(open("listPages/"+file, 'r'), 'html.parser')
    itemList = parsed.findAll(attrs={'class':'product--title'})
    for item in itemList:
        bicycle = {
            'title': '',
            'url': ''
        }  
        bicycle['title'] = item['title']
        bicycle['url'] = item['href']
        bicycles.append(bicycle)

modelDownloader = open('modelDownloader.py', 'w')
modelDownloader.write("import os\nbicycles = "+str(bicycles))