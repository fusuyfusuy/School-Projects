from bs4 import BeautifulSoup
import unicodecsv as csv
import sys
import time
import re
import os
import json

loopcount = len(sys.argv)
k = 1
while (k<loopcount):
    personId = os.path.basename(str(sys.argv[k]))
    personId = os.path.splitext(personId)[0]
    try:
        print("working on "+str(sys.argv[k]))
        html = open(str(sys.argv[k])).read()
        soup = BeautifulSoup(html, "lxml")
        infoParent = soup.find_all("div", {"class": "col-md-8 col-xs-12 edit-list-section"})[0]
        # age and gender . ile ayrilacak farkli datalar

        personDict = {
            '_id': personId,
            'info': {
                'name':'',
                'availableDate':'',
                'age':'',
                'gender':'',
                'smoking':'',
                'pets':'',
                'employment':'',
                'interests':[]
            },
            'search': {
                'home': {
                    'rent':'',
                    'bedroomType':'',
                    'homeSizes':[],
                    'bedroomSizes':[],
                    'bedroomFurniture':[],
                    'bathroomFacilities':[],
                    'parkingFacilities':[],
                },
                'flatmate': {
                    'gender':'',
                    'ageGroup':'',
                    'smoking':'',
                    'pets':''
                },
                'location': []
            }
        }

        personName = soup.find_all("h1", {"class":"edit-list-title"})[0].text.strip()

        personDict['info']['name']=personName

        # ilk blok
        info1 = infoParent.contents[1].contents[3]
        personDataMain = info1.find_all("div",{"class":"edit-list-box edit-third"})[0].contents[1].contents[1]
        personDataQ = []
        personDataA = []
        personQAData = personDataMain.find_all("div",{"class":"col-xs-12"})
        for i in range(len(personQAData)):
            if(i%3==0):
                personDataQ.append(personQAData[i].contents[1].text.strip())
                personDataA.append(personQAData[i].contents[3])

        for i in range(len(personDataA)):
            listFind = personDataA[i].find_all("li") 
            if(len(listFind)!=0):
                tempArr = []
                for j in range(len(listFind)):
                    tempArr.append(listFind[j].text.strip())
                # tempStr = '["'+'", "'.join(tempArr)+'"]'
                personDataA[i] = tempArr
            else:
                personDataA[i] = personDataA[i].text.strip()

        personDict['info']['availableDate']=personDataA[0]
        personDict['info']['age']=personDataA[1]
        personDict['info']['gender']=personDataA[1]
        personDict['info']['smoking']=personDataA[2]
        personDict['info']['pets']=personDataA[3]
        personDict['info']['employment']=personDataA[4]
        personDict['info']['interests']=personDataA[5]


        # about this person dahil alttaki 4 blok
        info2 = infoParent.find_all("div",{"class":"edit-list-box edit-fourth"})
        aboutPersonQ = []
        aboutPersonA = []
        for i in range(len(info2)):
            aboutPersonQ.append(info2[i].find_all("div",{"class":"col-xs-10 lower-title"})[0].text.strip())
            aboutPersonA.append(info2[i].find_all("div",{"class":"col-xs-12 col-sm-12 edit-fo-details"})[0].text.strip())



        info3 = infoParent.find_all("div",{"class":"edit-list-box edit-sixth"})

        # home preference
        homeDataMain = info3[0].find_all("div",{"class":"float-left width100 lower-border"})
        homeDataQ = []
        homeDataA = []
        for i in range(len(homeDataMain)):
            # homeDataQ.append(homeDataMain[i].find_all("div",{"class":"col-md-4 col-sm-4 col-xs-12 paddingleft-10 lower-title"})[0].text.strip())
            # homeDataA.append(homeDataMain[i].find_all("div",{"class":"col-md-8 col-sm-8 col-xs-12 lower-details color-dot"})[0])
            homeDataQ.append(homeDataMain[i].contents[1].text.strip())
            homeDataA.append(homeDataMain[i].contents[3])
        for i in range(len(homeDataA)):
            listFind = homeDataA[i].find_all("li") 
            if(len(listFind)!=0):
                tempArr = []
                for j in range(len(listFind)):
                    tempArr.append(listFind[j].text.strip())
                # tempStr = '["'+'", "'.join(tempArr)+'"]'
                homeDataA[i] = tempArr
            else:
                homeDataA[i] = homeDataA[i].text.strip()


        personDict['search']['home']['rent']=homeDataA[0]
        personDict['search']['home']['bedroomType']=homeDataA[1]
        personDict['search']['home']['homeSizes']=homeDataA[2]
        personDict['search']['home']['bedroomSizes']=homeDataA[3]
        personDict['search']['home']['bedroomFurniture']=homeDataA[4]
        personDict['search']['home']['bathroomFacilities']=homeDataA[5]
        personDict['search']['home']['parkingFacilities']=homeDataA[6]



        # flatmate preferences
        flatMain = info3[1].find_all("div",{"class":"float-left width100 lower-border"})
        flatQ = []
        flatA = []
        for i in range(len(flatMain)):
            # flatQ.append(flatMain[i].find_all("div",{"class":"col-md-4 col-sm-4 col-xs-12 paddingleft-10 lower-title"})[0].text.strip())
            # flatA.append(flatMain[i].find_all("div",{"class":"col-md-8 col-sm-8 col-xs-12 lower-details color-dot"})[0])
            flatQ.append(flatMain[i].contents[1].text.strip())
            flatA.append(flatMain[i].contents[3])
        for i in range(len(flatA)):
            listFind = flatA[i].find_all("li") 
            if(len(listFind)!=0):
                tempArr = []
                for j in range(len(listFind)):
                    tempArr.append(listFind[j].text.strip())
                # tempStr = '["'+'", "'.join(tempArr)+'"]'
                flatA[i] = tempArr
            else:
                flatA[i] = flatA[i].text.strip()


        personDict['search']['flatmate']['gender']=flatA[0]
        personDict['search']['flatmate']['ageGroup']=flatA[1]
        personDict['search']['flatmate']['smoking']=flatA[2]
        personDict['search']['flatmate']['pets']=flatA[3]


        # location preferences
        locMain = infoParent.find_all("div",{"class":"edit-list-box edit-nine"})[0]
        locQ = "Location Preferences"
        locA = []
        listFind = locMain.find_all("li") 
        if(len(listFind)!=0):
            tempArr = []
            for j in range(len(listFind)):
                tempArr.append(listFind[j].text.strip())
            # tempStr = '["'+'", "'.join(tempArr)+'"]'
            locA = tempArr
        else:
            locA = "No answer"

        personDict['search']['location']=locA
        # personDataQ = '['+', '.join(personDataQ)+']'
        # personDataA = '['+', '.join(personDataA)+']'
        # aboutPersonQ = '['+', '.join(aboutPersonQ)+']'
        # aboutPersonA = '['+', '.join(aboutPersonA)+']'
        # homeDataQ = '['+', '.join(homeDataQ)+']'
        # homeDataA = '['+', '.join(homeDataA)+']'
        # flatQ = '['+', '.join(flatQ)+']'
        # flatA = '['+', '.join(flatA)+']'
        # # locA = '["'+'", "'.join(locA)+'"]'

        # with open('maindata.csv', mode='a') as f:
        #     writer = csv.writer(f, encoding='utf-8')
        #     # writer.writerow(["id","person name",personDataQ,homeDataQ,flatQ,locQ])
        #     writer.writerow([personId,personName,personDataA,homeDataA,flatA,locA])

        personJSON = json.dumps(personDict, ensure_ascii=False, indent = 5)
        # print(personJSON)
        with open('personJSON.json','a') as outfile:
            json.dump(personDict, outfile)
            outfile.write(', \n')
        personDict = ''

    except:
        print('error on:   '+ personId)
    k=k+1
