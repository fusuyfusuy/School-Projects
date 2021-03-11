from bs4 import BeautifulSoup
import os
import wget
from urllib.request import Request, urlopen

bicycles = []

for i in range(73):
    listFile = open("./epeyListPages/epey"+str(i+1)+".html","r")
    listFileParser = BeautifulSoup(listFile, "html.parser")
    listItems = listFileParser.findAll(attrs={"class": "urunadi"})
    for item in listItems:
        bicycles.append({
            'name': item['title'],
            'link': item['href']
        })
    listFile.close()



howMany = 10
divided = []
for i in range(howMany):
    divided.append([])
counter = 0
for i in bicycles:
    which = counter%howMany
    divided[which].append({
        "name":i['name'],
        "link":i['link']
    })
    counter+=1


counter = 0
for i in divided:
    stringToFile = """
from bs4 import BeautifulSoup
import os
import wget
from urllib.request import Request, urlopen

bicycles="""
    stringToFile += str(i)
    stringToFile += """

for i in bicycles:
    url = i['link']
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print("err in    "+i['link'])
    else:
        print("Downloaded  "+i['name']+"                                                                                        ", end="\\r")
    fileName = i['name'].replace('/','_')
    f = open("./listItems/"+fileName+'.html', 'wb')
    f.write(webpage)
    f.close
"""
    theFile = open("downLink"+str(counter)+".py","w")
    theFile.write(stringToFile)
    theFile.close()
    counter+=1

downloaderFile = open("startDownload.sh",'a')
downloaderFile.write("#!/bin/bash\n")
for i in range(len(divided)):
    stringToAdd = "\npython3 downLink"+str(i)+".py &"
    downloaderFile.write(stringToAdd)

# url = bicycles[0]['link']
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# f = open("./listItems/"+bicycles[0]['name']+'.html', 'wb')
# f.write(webpage)
# f.close