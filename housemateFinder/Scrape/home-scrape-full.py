from bs4 import BeautifulSoup
import unicodecsv as csv
import sys
import time
import re
import os
import json

loopcount = len(sys.argv)
j = 1
while (j < loopcount):
    homeid = os.path.basename(str(sys.argv[j]))
    homeid = os.path.splitext(homeid)[0]
    try:
        # print("working on "+str(sys.argv[j]))
        html = open(str(sys.argv[j])).read()
        soup = BeautifulSoup(html, "lxml")
        infoParent = soup.find_all("div", {"class": "col-lg-8 col-xs-12 edit-main-section"})

        homeDict = {
            '_id': homeid,
            'info': {
                'city': '',
                'block': '',
                'homeType': '',
                'homeSize': '',
                'parking': ''
            },
            'bedroomInfo': {
                'rent': '',
                'dateAvailable': '',
                'bedroomSize': '',
                'bedroomFurniture': '',
                'features': '',
                'bond': '',
                'otherInformation': ''
            },
            'description': {
                'homeDescription': '',
                'features': '',
                'bills': ''
            },
            'occupants': {
                'gender': '',
                'age': '',
                'smoking': '',
                'pets': '',
                'interests': '',
                'about': '',
                'compatiblePeople': '',
            },
            'flatmatePreferences': {
                'gender': '',
                'age': '',
                'smoking': '',
                'pets': ''
            }
        }

        houseInfo = soup.find_all("div", {"class": "col-lg-8 col-xs-12"})
        sehir = houseInfo[0].p.text  # sehir
        mahalle = houseInfo[0].h1.text.strip()  # mahalle
        hometypeQ = houseInfo[0].find_all(
            "div", {"class": "second-text-one"})  # hometype falan
        hometypeQText = []
        for i in hometypeQ:
            hometypeQText.append(i.text.strip())
        hometypeA = houseInfo[0].find_all(
            "div", {"class": "second-text-two"})  # cevaplari
        hometypeAText = []
        for i in hometypeA:
            hometypeAText.append(i.text.strip())

        homeDict['info']['city'] = sehir
        homeDict['info']['block'] = mahalle
        homeDict['info']['homeType'] = hometypeAText[0]
        homeDict['info']['homeSize'] = hometypeAText[1]
        homeDict['info']['parking'] = hometypeAText[2]

        # private bedroom
        info1 = infoParent[0].contents[1].contents[1]
        # private bedroom baslik ama hatali
        privateBedroomBaslik = info1.contents[1].contents[1].h3.text
        privateBedroomBaslikClean = privateBedroomBaslik.splitlines()[
            1].strip()
        # privateBedroomBaslikClean = privateBedroomBaslik.split()[0]+" "+privateBedroomBaslik.split()[1]
        privateBedroomQ = info1.contents[1].find_all(
            "div", {"class": "col-md-3 col-sm-3 col-xs-12 paddingleft-10 lower-title"})
        privateBedroomQLenght = len(privateBedroomQ)
        privateBedroomA = info1.contents[1].find_all(
            "div", {"class": "col-md-9 col-sm-9 lower-details"})
        if privateBedroomQLenght > len(privateBedroomA):
            for i in range(len(privateBedroomQ)-len(privateBedroomA)):
                privateBedroomA.append(info1.contents[1].find_all(
                    "div", {"class": "col-md-9 col-sm-9 lower-details more"})[i])
        privateBedroomQText = []
        for i in privateBedroomQ:
            privateBedroomQText.append(i.text.strip())
        privateBedroomAText = []
        for i in privateBedroomA:
            privateBedroomAText.append(i.text.strip())
        for i in range(len(privateBedroomA)):
            if len(privateBedroomA[i].find_all("li")) != 0:
                arrpb = []
                pbli = privateBedroomA[i].find_all("li")
                rangelen = len(pbli)
                for k in range(rangelen):
                    arrpb.append(pbli[k].text.strip())
                pbstr = '["'+'", "'.join(arrpb)+'"]'
                privateBedroomAText[i] = arrpb
        if len(privateBedroomA[0].contents[1]) == 5:
            pbrent = privateBedroomA[0].contents[1]
            pbrentarr = []
            pbrentarr.append(pbrent.contents[1].text.strip())
            pbrentarr.append(pbrent.contents[3].text.strip())
            pbrentstr = '["'+'", "'.join(pbrentarr)+'"]'
            privateBedroomAText[0] = pbrentarr

        homeDict['bedroomInfo']['rent'] = privateBedroomAText[0]
        homeDict['bedroomInfo']['dateAvailable'] = privateBedroomAText[1]
        homeDict['bedroomInfo']['bedroomSize'] = privateBedroomAText[2]
        homeDict['bedroomInfo']['bedroomFurniture'] = privateBedroomAText[3]
        homeDict['bedroomInfo']['features'] = privateBedroomAText[4]
        homeDict['bedroomInfo']['bond'] = privateBedroomAText[5]
        if(len(privateBedroomAText) == 7):
            homeDict['bedroomInfo']['otherInformation'] = privateBedroomAText[6]

        # home description
        # home description
        info2 = infoParent[0].contents[1].contents[3].contents[1]
        # home description baslik
        descriptionBaslik = info2.contents[1].text.strip()
        # home description icerik
        descriptionIcerik = info2.contents[3].contents[1].text.strip()
        di = descriptionIcerik.encode('ascii', 'ignore')
        descriptionIcerik = str.join(" ", di.splitlines())
        # home features baslik
        featuresBaslik = info2.contents[3].contents[3].contents[1].text.strip()
        featuresIcerik = info2.contents[3].contents[3].contents[3].find_all(
            "li")  # home features icerik liste
        # bills and expenses baslik
        billsBaslik = info2.contents[3].contents[5].contents[1].text.strip()
        # bills and expenses icerik
        billsIcerik = info2.contents[3].contents[5].contents[3].text.strip()
        featuresIcerikText = []
        for i in featuresIcerik:
            featuresIcerikText.append(i.text.strip())

        homeDict['description']['homeDescription'] = descriptionIcerik
        homeDict['description']['features'] = featuresIcerikText
        homeDict['description']['bills'] = billsIcerik

        # occupant info
        info3 = infoParent[0].contents[1].contents[5].contents[1]
        # occupant description baslik
        occupantBaslik = info3.contents[1].text.strip()
        occupantQ = info3.contents[3].find_all(
            "div", {"class": "col-md-3 col-sm-3 col-xs-12 paddingleft-10 lower-title"})
        occupantQL = len(occupantQ)
        occupantA = info3.contents[3].find_all(
            "div", {"class": "col-md-9 col-sm-9 lower-details"})
        occupantAL = len(occupantA)
        occupantDiff = occupantQL-occupantAL
        occupantA2 = info3.contents[3].find_all(
            "div", {"class": "col-md-9 col-sm-9 lower-details more"})
        for i in range(occupantDiff):
            occupantA.append(occupantA2[i])
        occupantAText = []
        occupantQText = []
        for i in occupantQ:
            occupantQText.append(i.text.strip())
        for i in range(len(occupantA)):
            if i == 4:
                occupantAText.append("")
                continue
            occupantAText.append(occupantA[i].text.strip())
        occ4 = occupantA[4].find_all("li")
        arr4 = []
        lenocc4 = len(occ4)
        for i in range(lenocc4):
            arr4.append(occ4[i].text.strip())
        arr4str = '["'+'", "'.join(arr4)+'"]'
        occupantAText[4] = arr4
        occ0 = occupantA[0].find_all("li")
        occ0len = len(occ0)
        if occ0len != 0:
            arr0 = []
            for i in range(occ0len):
                arr0.append(occ0[i].text.strip())
            arr0str = '["'+'", "'.join(arr0)+'"]'
            occupantAText[0] = arr0
        occ1 = occupantA[1].find_all("li")
        occ1len = len(occ1)
        if occ1len != 0:
            arr1 = []
            for i in range(occ1len):
                arr1.append(occ1[i].text.strip())
            arr1str = '["'+'", "'.join(arr1)+'"]'
            occupantAText[1] = arr1
        for i in range(len(occupantA)):
            if len(occupantA[i].find_all("li")) != 0:
                arroc = []
                lioc = occupantA[i].find_all("li")
                rangelen = len(lioc)
                for k in range(rangelen):
                    arroc.append(lioc[k].text.strip())
                ocstr = '["'+'", "'.join(arroc)+'"]'
                occupantAText[i] = arroc

        homeDict['occupants']['gender'] = occupantAText[0]
        homeDict['occupants']['age'] = occupantAText[1]
        homeDict['occupants']['smoking'] = occupantAText[2]
        homeDict['occupants']['pets'] = occupantAText[3]
        homeDict['occupants']['interests'] = occupantAText[4]
        homeDict['occupants']['about'] = occupantAText[5]
        homeDict['occupants']['compatiblePeople'] = occupantAText[6]
        if(len(occupantAText) == 8):
            homeDict['occupants']['petDescription'] = occupantAText[7]

        # flatmate info
        info4 = infoParent[0].contents[1].contents[7].contents[1]
        # flatmate preferences baslik
        flatmateBaslik = info4.contents[1].text.strip()
        flatmateQ = info4.contents[3].find_all(
            "div", {"class": "col-md-3 col-sm-3 col-xs-12 paddingleft-10 lower-title"})
        flatmateA = info4.contents[3].find_all(
            "div", {"class": "col-md-9 col-sm-9 lower-details"})
        flatmateQText = []
        flatmateAText = []
        for i in flatmateQ:
            flatmateQText.append(i.text.strip())
        for i in flatmateA:
            flatmateAText.append(i.text.strip())
        flat0 = flatmateA[0].find_all("li")
        flat0len = len(flat0)
        if flat0len != 0:
            flat0arr = []
            for i in range(flat0len):
                flat0arr.append(flat0[i].text.strip())
            flat0str = '["'+'", "'.join(flat0arr)+'"]'
            flatmateAText[0] = flat0arr
        flat2 = flatmateA[2].find_all("li")
        flat2len = len(flat2)
        if flat2len != 0:
            flat2arr = []
            for i in range(flat2len):
                flat2arr.append(flat2[i].text.strip())
            flat2str = '["'+'", "'.join(flat2arr)+'"]'
            flatmateAText[2] = flat2arr
        flat3 = flatmateA[3].find_all("li")
        flat3len = len(flat3)
        if flat3len != 0:
            flat3arr = []
            for i in range(flat3len):
                flat3arr.append(flat3[i].text.strip())
            flat3str = '["'+'", "'.join(flat3arr)+'"]'
            flatmateAText[3] = flat3arr
        for i in range(len(flatmateA)):
            if len(flatmateA[i].find_all("li")) != 0:
                arrflat = []
                liflat = flatmateA[i].find_all("li")
                rangelen = len(liflat)
                for k in range(rangelen):
                    arrflat.append(liflat[k].text.strip())
                # flatstr = '["'+'", "'.join(arrflat)+'"]'
                flatmateAText[i] = arrflat

        homeDict['flatmatePreferences']['gender'] = flatmateAText[0]
        homeDict['flatmatePreferences']['age'] = flatmateAText[1]
        homeDict['flatmatePreferences']['smoking'] = flatmateAText[2]
        homeDict['flatmatePreferences']['pets'] = flatmateAText[3]

        # strHomeA = '["'+'", "'.join(hometypeAText)+'"]'
        # strHomeQ = '["'+'", "'.join(hometypeQText)+'"]'
        # strpbQ = '["'+'", "'.join(privateBedroomQText)+'"]'
        # strpbA = '["'+'", "'.join(privateBedroomAText)+'"]'
        # strfeatures = '["'+'", "'.join(featuresIcerikText)+'"]'
        # stroccQ = '["'+'", "'.join(occupantQText)+'"]'
        # stroccA = '["'+'", "'.join(occupantAText)+'"]'
        # strflatQ = '["'+'", "'.join(flatmateQText)+'"]'
        # strflatA = '["'+'", "'.join(flatmateAText)+'"]'

        # with open('maindata.csv', mode='a') as f:
        #     writer = csv.writer(f, encoding='utf-8')
        #     # writer.writerow([strflatQ,strflatA])
        #     writer.writerow([homeid, sehir, mahalle, strHomeQ, strHomeA, privateBedroomBaslikClean, strpbQ, strpbA,descriptionBaslik, descriptionIcerik, featuresBaslik, strfeatures,billsBaslik,billsIcerik,occupantBaslik,stroccQ,stroccA,flatmateBaslik,strflatQ,strflatA,])
        #     # writer.writerow(['city','block',strHomeQ,'bedroom type',strpbQ,'home description','home features','bills and expenses',stroccQ,strflatQ])
        # # print([sehir, mahalle, strHomeQ, strHomeA, privateBedroomBaslikClean, strpbQ, strpbA,descriptionBaslik, descriptionIcerik, featuresBaslik, strfeatures,billsBaslik,billsIcerik,occupantBaslik,stroccQ,stroccA,flatmateBaslik,strflatQ,strflatA,])

        # homeid,
        # sehir,
        # mahalle,
        # strHomeQ,
        # strHomeA,
        # privateBedroomBaslikClean,
        # strpbQ,
        # strpbA,
        # descriptionBaslik,
        # descriptionIcerik,
        # featuresBaslik,
        # strfeatures,
        # billsBaslik,
        # billsIcerik,
        # occupantBaslik,
        # stroccQ,
        # stroccA,
        # flatmateBaslik,
        # strflatQ,
        # strflatA
        # dataArray = [homeid,sehir,mahalle,hometypeQText,hometypeAText,privateBedroomBaslikClean,privateBedroomQText,privateBedroomAText,descriptionBaslik,descriptionIcerik,featuresBaslik,featuresIcerikText,billsBaslik,billsIcerik,occupantBaslik,occupantQText,occupantAText,flatmateBaslik,flatmateQText,flatmateAText]
        # for data in dataArray:
        #     if(type(data) is list):
        #         for dataData in data:
        #             if(type(dataData) is list):
        #                 print(dataData)

        homeJSON = json.dumps(homeDict, ensure_ascii=False, indent=5)
        # print(homeJSON)
        with open('homeJSON-a.json', 'a') as outfile:
            json.dump(homeDict, outfile)
            outfile.write(', \n')

        homeDict=''

    except Exception as e:
        print('error on:   ' + homeid)
        print(e)
    j = j+1
