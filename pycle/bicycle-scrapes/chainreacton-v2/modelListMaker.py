import os
from bs4 import BeautifulSoup


fileList = os.listdir('listPages')
modelList = []

for f in fileList:
    type = os.listdir('listPages/'+f)
    for b in type:
        html = open('listPages/'+f+'/'+b, 'r')
        parsed = BeautifulSoup(html, 'html.parser')
        products = parsed.findAll(attrs={'class':'products_details'})
        for i in products:
            model = {
                'title': '',
                'url': '',
                'type': ''
            }
            url = i.find(attrs={'class':'description'})
            model['url'] = url.find('a')['href']
            model['title'] = url.text.strip().replace('\n','')
            model['type'] = f
            modelList.append(model)

modelFile = open('modelList.py','w')
modelFile.write("""
import os
links = """)

for i in modelList:
    modelFile.write(str(i)+',\n')