from bs4 import BeautifulSoup
import os 
import csv

bicycles = []
basepath = 'HTMLFiles/'
outputFile = open('scraped.py','a')
outputFile.write("list=[")
len1 = len(os.listdir(basepath))
counter1 = 0
for entry in os.listdir(basepath):
    counter2 = 0
    len2 = len(os.listdir(basepath+'/'+entry))
    for folder in os.listdir(basepath+'/'+entry):
        listFile = open(basepath+entry+'/'+folder,"r")
        try:
            parsed = BeautifulSoup(listFile, "html.parser")
        except:
            print('bs4 error in '+basepath+entry+'/'+folder)
            break
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

        tableRows = parsed.findAll('tr')
        
        for row in tableRows:
            tableData = row.findAll('td')
            try:
                key = tableData[0].text.strip()
                value = tableData[1].text.strip()
            except:
                print('error in '+basepath+entry+'/'+folder)
                break
            else:
                bicycle[key] = value

        if(bicycle['Brand']!='-'):
            bicycles.append(bicycle)
            outputFile.write(str(bicycle)+',\n')
        counter2+=1
        print("parsing "+str(counter2)+" of "+str(len2)+"                              ", end='\r')
    counter1+=1
    print("\nFOLDER parsing "+str(counter1)+" of "+str(len1)+"                              \n", end='\r')



# keys = bicycles[0].keys()
# with open('bicycles.csv', 'w', newline='')  as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(bicycles)

outputFile.write(']')
toWrite = """
import csv
keys = list[0].keys()
with open('bicycles.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list)
"""
outputFile.write(toWrite)