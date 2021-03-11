from bs4 import BeautifulSoup
import os 

bicycle = {
    'Brand': '-',
    'Model': '-',
    'Weight': '-',
    'Released on the market': '-',
    'For women': '-',
    'For kids': '-',

    'Frame material': '-',
    'Frame type': '-',
    'Collapsible frame': '-',
    'Color': '-',

    'Fork type': '-',
    'Shock absorber type': '-',
    'Shock absorber pressure': '-',
    'Fork name': '-',

    'Wheel drive': '-',
    'Drive type': '-',
    'Transmission type': '-',
    'Number of speeds': '-',
    'System name': '-',
    'Cassette name': '-',
    'Front derailleur gears name': '-',
    'Rear derailleur gears name': '-',

    'Shifters type': '-',
    'Shifters name': '-',

    'Front brakes': '-',
    'Front brakes name': '-',
    'Rear brakes': '-',

    'Number of wheels': '-',
    'Wheels diameter': '-',
    'Double rim': '-',
    'Rim material': '-',
    'Rims name': '-',
    'Tyres pattern': '-',
    'Tyres name': '-',

    'Handlebar type': '-',
    'Handlebar name': '-',

    'Seat type': '-',
    'Seat suspension': '-',
    'Seat name': '-',

    'Pedals type': '-',
    'Pedals name': '-',

    'Front panel': '-',
    'Rear panel panel': '-',
    'Trunk': '-',
    'Rearview mirror': '-',
    'Horn': '-',
    'Basket': '-'
}

htmlFile = open("./Infinito Athena Compact (2012).html.html",'r')
parsed = BeautifulSoup(htmlFile, "html.parser")

tableRows = parsed.findAll('tr')
for row in tableRows:
    tableData = row.findAll('td')
    key = tableData[0].text.strip()
    value = tableData[1].text.strip()
    bicycle[key] = value

