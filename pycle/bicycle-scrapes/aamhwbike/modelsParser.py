import os
from bs4 import BeautifulSoup
import csv

bicycles = []
fileList = os.listdir('models')
counter = 0
for file in fileList:
    print('working on', counter, 'for ', len(fileList))
    counter += 1
    bicycle = {'Price': '------', 'Brand': '------', 'Model': '------', 'Frame': '------', 'Color': '------', 'Size': '------', 'Fork': '------', 'Headset': '------', 'Stem': '------', 'Handlebar': '------', 'Grips': '------', 'Rear Derailleur': '------', 'Front Derailleur': '------', 'Shifter': '------', 'Brake': '------', 'Crankset': '------', 'Cassette': '------', 'Chain': '------', 'Rims': '------', 'Hub Front': '------', 'Hub Rear': '------', 'Tires': '------', 'Pedals': '------', 'Saddle': '------', 'Seat Post': '------', 'Seat Post Clamp': '------', 'Weight (KG)': '------', 'Bike Type:': '------', 'Target Group:': '------', 'Material:': '------', 'Wheel Size:': '------', 'Model year:': '------', 'Front Light': '------', 'Rear Light': '------', 'Kickstand': '------', 'Mudguards': '------', 'Bell': '------', 'Other properties:': '------', 'Tire Front': '------', 'Tire Rear': '------', 'Wheelset': '------', 'Rack': '------', 'Handlebaraufsatz': '------', 'Handlebarband': '------', 'Shifter/Brakelever': '------', 'Brake-Type:': '------', 'Brakes': '------', 'Brake Lever': '------', 'Shock': '------', 'Shock-hardware': '------', 'Hubsritzel': '------', 'Chain Guide': '------', 'Number of gears': '------', 'Bottom Bracket': '------', 'Brake Discs': '------', 'Front rim': '------', 'Rim rear': '------', 'Spokes': '------', 'Drive Unit': '------', 'Battery': '------', 'Display': '------', 'Charger': '------', 'Derailleur hanger': '------', 'Maximum weight allowed': '------', 'Chain Guard': '------', 'Weight (LBS)': '------'}

    parsed = BeautifulSoup(open('models/'+file), 'html.parser')

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
    bicycles.append(bicycle)

keys = bicycles[0].keys()
with open('bicycles.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(bicycles)
