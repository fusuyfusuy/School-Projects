from bs4 import BeautifulSoup
import os


listFile = open('Blank Digit BMX Bike.html')
parsed = BeautifulSoup(listFile, 'html.parser')

features = parsed.find(text="Features:").findNext('ul')
featureList = features.findAll('li')
for i in featureList:
    title = i.text.split(': ', 1)[0]
    detail = i.text.split(': ', 1)[1]

# print(parsed.find('h1').text.strip().replace('\n',' &&&& ').split(' &&&& ')[1])


price = parsed.find(attrs={'class':'crcPDPPriceHidden'})

print(price.text.strip().replace('\n',''))