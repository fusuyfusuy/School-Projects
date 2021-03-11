import os
from bs4 import BeautifulSoup


fileList = os.listdir('listPages')
modelList = []

for f in fileList:
    html = open('listPages/'+f, 'r')
    parsed = BeautifulSoup(html, 'html.parser')
    products = parsed.findAll(attrs={'class':'products_details'})
    for i in products:
        model = {
            'title': '',
            'url': ''
        }
        url = i.find(attrs={'class':'description'})
        model['url'] = url.find('a')['href']
        model['title'] = url.text.strip().replace('\n','')
        modelList.append(model)

modelFile = open('modelList.py','w')
modelFile.write("""
import os
links = """)

for i in modelList:
    modelFile.write(str(i)+',\n')