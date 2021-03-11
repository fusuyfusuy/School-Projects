import os
from bs4 import BeautifulSoup

bicycle = {'Price':'------','Brand':'------','Model':'------','Frame': '------', 'Color': '------', 'Size': '------', 'Fork': '------', 'Headset': '------', 'Stem': '------', 'Handlebar': '------', 'Grips': '------', 'Rear Derailleur': '------', 'Front Derailleur': '------', 'Shifter': '------', 'Brake': '------', 'Crankset': '------', 'Cassette': '------', 'Chain': '------', 'Rims': '------', 'Hub Front': '------', 'Hub Rear': '------', 'Tires': '------', 'Pedals': '------', 'Saddle': '------', 'Seat Post': '------', 'Seat Post Clamp': '------', 'Weight (KG)': '------', 'Bike Type:': '------', 'Target Group:': '------', 'Material:': '------', 'Wheel Size:': '------', 'Model year:': '------'}

parsed = BeautifulSoup(open('Cube Access WS Exc black n blue - Hardtail Mountainbike Women.html'), 'html.parser')

description = parsed.find(attrs={'class':'product--description'}).findAll('tr')
properties = parsed.find(attrs={'class':'product--properties'}).findAll('tr')

for d in description:
    data = d.findAll('td')
    try:
        key = data[0].text.strip()
        value = data[1].text.strip()
    except:
        print(data)
    else:
        bicycle[key] = value

for p in properties:
    data = p.findAll('td')
    try:
        key = data[0].text.strip()
        value = data[1].text.strip()
    except:
        print(data)
    else:
        bicycle[key] = value