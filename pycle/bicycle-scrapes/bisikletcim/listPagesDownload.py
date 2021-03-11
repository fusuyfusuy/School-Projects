from bs4 import BeautifulSoup
import wget
import os


base = 'https://www.bisikletcim.com/'
dag = 'dag-bisikleti' # 13 sayfa 
sehir = 'sehir-tur-bisikleti' # 7 sayfa 
yol = 'yol-yaris-bisikleti' # 2 sayfa
cocuk1 = 'cocuk-bisikleti/7-12-yas-20-jant-bisiklet' # 3 sayfa
cocuk2 = 'cocuk-bisikleti/4-7-yas-16-jant-bisiklet' # 2 sayfa
cocuk3 = 'cocuk-bisikleti/1-4-yas-12-14-jant-bisiklet' # 2 sayfa
cocuk4 = 'uc-tekerlekli-cocuk-bisikleti' # 1 sayfa

# for i in range(13):
#     wget.download(base+dag+"?rpg="+str(i+1), out=dag+str(i+1)+'.html')

# for i in range(7):
#     wget.download(base+sehir+"?rpg="+str(i+1), out='lists/'+sehir+str(i+1)+'.html')

# for i in range(2):
#     wget.download(base+yol+"?rpg="+str(i+1), out='lists/'+yol+str(i+1)+'.html')

# for i in range(3):
#     wget.download(base+cocuk1+"?rpg="+str(i+1), out='lists/'+'cocuk7-12'+str(i+1)+'.html')

# for i in range(2):
#     wget.download(base+cocuk2+"?rpg="+str(i+1), out='lists/'+'cocuk2'+str(i+1)+'.html')

# for i in range(2):
#     wget.download(base+cocuk3+"?rpg="+str(i+1), out='lists/'+'cocuk3'+str(i+1)+'.html')

# for i in range(1):
#     wget.download(base+cocuk4+"?rpg="+str(i+1), out='lists/'+'cocuk4'+str(i+1)+'.html')

modelUrls = []

fileList = os.listdir('lists/')

for f in fileList:
    page = open('lists/'+f)
    parsed = BeautifulSoup(page, 'html.parser')
    itemList = parsed.findAll(attrs={"class": "item"})
    for item in itemList:
        model = {
            'title': '',
            'url': ''
        }
        model['title'] = item.find('a')['title']
        model['url'] = item.find('a')['href']
        modelUrls.append(model)

modelSave = open('modelsave.py', 'w')
modelSave.write("modelUrls = [\n")
for i in modelUrls:
    modelSave.write(str(i)+',\n')
modelSave.write('\n]')