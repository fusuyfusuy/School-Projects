from bs4 import BeautifulSoup
import os
import csv

bicycles = []
save = open('bicycleSave2.py','a')

types = os.listdir('modelDownload/modelPages')

for t in types:
    bType = '------'
    if str(t)=='bmx':
        bType = 'BMX'
    elif str(t)=='cross':
        bType = 'Cyclo Cross'
    elif str(t)=='electric':
        bType = 'Electric'
    elif str(t)=='folding':
        bType = 'Folding'
    elif str(t)=='hybrid' :
        bType = 'Hybrid - City'
    elif str(t)=='kid' :
        bType = 'Kids'
    elif str(t)=='mountain' :
        bType = 'Mountain'
    elif str(t)=='road' :
        bType = 'Road'
    elif str(t)=='tt' :
        bType = 'TT'

    files = os.listdir('modelDownload/modelPages/'+t)
    for f in files:
        listFile = open('modelDownload/modelPages/'+str(t)+'/'+str(f))
        print('parsing '+str(t)+'/'+str(f)+'                                                            ',end='\r')
        parsed = BeautifulSoup(listFile, 'html.parser')
        brand = parsed.find('h1').text.strip().replace('\n',' &&&& ').split(' &&&& ')[0]
        model = parsed.find('h1').text.strip().replace('\n',' &&&& ').split(' &&&& ')[1]
        try:
            price = parsed.find(attrs={'class':'crcPDPPriceHidden'}).text.strip().replace('\n','')
        except:
            print('price error on '+str(f))
            price = '------'
        # features
        try:
            features = parsed.find(text="Features:").findNext('ul')
            featureList = features.findAll('li')
        except:
            print('error on ' + str(f))
        else:
            bicycle = {'Price':price,'Brand':brand,'Model':model,'Type':bType,'Colour': '------', 'Wheel Size': '------', 'Frame Size': '------', 'Gender': '------', 'Speed': '------', 'Material': '------', 'Age Group': '------', 'Fork Travel': '------', 'Rear Travel': '------','Frame': '------', 'Forks': '------', 'Brake': '------', 'Cable': '------', 'Brake Levers': '------', 'Chainwheel': '------', 'Freewheel': '------', 'Chain': '------', 'Headset': '------', 'Crank': '------', 'Bottom Bracket': '------', 'Rims': '------', 'Front Hub': '------', 'Rear Hub': '------', 'Tyres': '------', 'Seat': '------', 'Handlebars': '------', 'Handlebar Stem': '------', 'Grips': '------', 'Pedal': '------', 'Fork': '------', 'Steerer': '------', 'Stem': '------', 'Handlebar': '------', 'Handlebar Tape': '------', 'Shifter/Brake Levers': '------', 'Brake System': '------', 'Front Derailleur': '------', 'Rear Derailleur': '------', 'Crankset': '------', 'Cassette': '------', 'Saddle': '------', 'Seatpost': '------', 'Tubeless Ready Tyres': '------', 'Tubeless Ready Wheels': '------', 'Pedals': '------', 'Dropouts/Axle Type': '------', 'Maximum Tyre Size': '------', 'Rear Pannier Rack Compatible': '------', 'Mudguards Compatible': '------', 'Replacement Gear Hanger': '------', 'Weight': '------', 'Drivetrain': '------', 'Chainset': '------', 'Shifters': '------', 'Wheelset': '------', 'Brakes': '------', 'Bars': '------', 'Use': '------', 'Brake Rotors': '------', 'Bar Tape': '------', 'Brake Caliper Mounts': '------', 'Wheels': '------', 'Axles': '------', 'Max Tyre Clearance': '------', 'Seat Clamp': '------', 'Cog': '------', 'Hub Spacing': '------', 'Gear/Brake Levers': '------', 'Tyre Clearance': '------', 'Seat Post': '------', 'Cable Routing': '------', 'Brake Fitment': '------', 'Components': '------', 'Disc Brakes': '------', 'Handle Bar': '------', 'Stem/Seatpost': '------', 'Fork Weight': '------', 'Frame Weight': '------', 'Chainring': '------', 'Hubs': '------', 'Spokes/Nipples': '------', 'Accessories': '------', 'Rear Shock': '------', 'ISCG Tabs': '------', 'Chainguide': '------', 'Spokes': '------', 'Front Tyre': '------', 'Rear Tyre': '------', 'Seat Post Clamp': '------', 'Warranty': '------', 'Maximum Tyre Sizes': '------', 'Carrier / Basket': '------', 'Mudguards': '------', 'Stand': '------', 'Additional': '------', 'Light Front': '------', 'Light Rear': '------', 'Front Light': '------', 'Rear Light': '------', 'Seatclamp': '------', 'Tyre': '------', 'Seatpost Clamp': '------', 'Kickstand': '------', 'Mudguard': '------', 'Bell': '------', 'Extras': '------', 'Includes': '------', 'Shift/Brake Levers': '------', 'Shift Brake Levers': '------', 'Manufacturer Part Numbers': '------', '17” Blue/Red': '------', '19” Blue/Red': '------', '21” Blue/Red': '------', '17” Black/Flash Yellow': '------', '19” Black/Flash Yellow': '------', '21” Black/Flash Yellow': '------', 'Carrier': '------', 'Carrier Rack': '------', 'Shock Hardware': '------', 'Front Derailluer': '------', 'Cranks': '------', 'Integrated Handlebar/Stem': '------', 'Shift/ Brake Levers': '------', 'Engine': '------', 'Battery': '------', 'Charger': '------', 'Display': '------', 'Shifter': '------', '50cm': '------', '53cm': '------', '56cm': '------', '59cm': '------', '62cm': '------', 'Chain Guide': '------', 'Front Tyres': '------', 'Rear Pannier Rack': '------', '54cm': '------', '58cm': '------', 'Lights': '------', 'Frameset': '------', 'Brake/Shift Levers': '------', 'Front Brake': '------', 'Rear Brake': '------', 'Geometry': '------', 'BB': '------', 'Sprocket': '------', 'Front Wheel': '------', 'Rear Wheel': '------', 'Misc': '------', 'Brakeset': '------', 'Brakset': '------', 'Gear Hanger Model Number': '------', 'Chain Device': '------', 'Cog Set': '------', 'Handebar': '------', 'Rear Cog': '------', 'Rear Cogs': '------', 'Rear Cassette': '------', 'Frame Material': '------', 'Top Tube Length': '------', 'Brake Lever': '------', 'Brake Cable': '------', 'Driver': '------', 'Front Rim': '------', 'Rear Rim': '------', 'Gyro Tabs': '------', 'Stuntpegs': '------', 'Chain Stay Length': '------', 'Headtube Angle': '------', 'Seat Tube Angle': '------', 'Gearing': '------', 'Crankarms': '------', 'Chainrings': '------', 'Brake Calipers': '------', 'Front Brake Rotor': '------', 'Rear Brake Rotor': '------', 'B/b': '------', 'B/B': '------', 'Sitting Posture': '------', 'Hub Type': '------', 'Number of Gears': '------', 'Brake Type': '------', 'Luggage Carrier': '------', 'Child Seat Compatible': '------', 'Front Seat Compatible': '------', 'Rear Seat Compatible': '------', 'Light': '------', 'Lock Type': '------', 'Suspension Fork': '------', 'Tyre Sealant': '------', 'Discs': '------', 'Battery Charger': '------', 'Brake Rotor': '------', 'Axle to Crown': '------', 'Fork Offset': '------', 'Max Tyre Size': '------', 'Protection': '------', 'Front Rotor': '------', 'Rear Rotor': '------', 'Brakes/Shifter': '------', 'Stem Lengths': '------', 'Shock': '------', 'Rear Deraileur': '------', 'Derailleurs': '------', 'Levers': '------', 'Shifter L': '------', 'Shifter R': '------', 'Brakes Front': '------', 'Brakes Rear': '------', 'Tubes': '------', 'Frame/Fork': '------', 'Brake Discs': '------', 'Groupset': '------', 'Derailleur Rear': '------', 'Axle Front': '------', 'Axle Rear': '------', 'Front Axle': '------', 'Rear Axle': '------', 'Suggested Rider Size': '------', 'Barends': '------', 'Pegs': '------', 'Top Tube': '------', 'Chain Stay': '------', 'Head Tube': '------', 'Seat Tube': '------', 'Brake Mounts': '------', 'Bar Ends': '------', 'Stand Over': '------', 'BB Height': '------', 'Head Tube Angle': '------', 'Standover Height': '------', 'Bottom Bracket Height': '------', 'Rear Lever': '------', 'Adjustable Stem': '------', 'Suspension Forks': '------', 'Grip(Tape)': '------', 'Spoke': '------', 'Front Brake Set': '------', 'Rear Brake Set': '------', 'Seat Screw': '------', 'Rear Shifter': '------', 'Rotors': '------', 'Grip (Tape)': '------', 'Left Shifter': '------', 'Right Shifter': '------', 'Rear rim': '------', 'Rear hub': '------', 'Rear Bbrake Set': '------', 'Front hub': '------', 'Tyre Type': '------', 'Minimum Saddle Height': '------', 'Maximum Saddle Height': '------', 'F/rim': '------', 'R/rim': '------', 'F/hub': '------', 'R/hub': '------', 'F/tire': '------', 'R/tire': '------', 'F/brake Set': '------', 'R/brake Set': '------', 'R/derailleur': '------', 'R/shifter': '------', 'Ideal Rider Inside Leg Length': '------'}
            for i in featureList:
                try:
                    title = i.text.split(':', 1)[0].strip()
                    detail = i.text.split(':', 1)[1].strip()
                    bicycle[title] = detail
                except:
                    print('        feature error on ' + str(f))
                else:
                    try:
                        featuresSpec = parsed.find(text="Specs").findNext('ul')
                        featureListSpec = featuresSpec.findAll('li')
                    except:
                        print('         specs error on ' + str(f))
                    else:
                        for j in featureListSpec:
                            try:
                                titleSpec = j.text.split(':', 1)[0].strip()
                                detailSpec = j.text.split(':', 1)[1].strip()
                                bicycle[titleSpec] = detailSpec
                            except:
                                print('                     specs error on ' + str(f))
            bicycles.append(bicycle)
            save.write(str(bicycle)+',\n')


# keys = bicycles[0].keys()
# with open('bicycles.csv', 'w', newline='')  as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(bicycles)
