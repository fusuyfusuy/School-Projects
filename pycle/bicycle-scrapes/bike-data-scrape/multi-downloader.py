from bs4 import BeautifulSoup
import wget
import os
from os import path

# # download main page
# print("Start   --  Downloading main page")
# try:
#     wget.download("http://bike-data.com/en", out="./main.html")
# except:
#     print("Error -- downloading main page")
#     quit()
# else:
#     print("Success\n")

# parse main page
mainPage = open("main.html", "r")
main = BeautifulSoup(mainPage, "html.parser")
bicycles = {}

# find brand pages
print("Start   -- finding brand pages")
try:
    brandPages = main.findAll('td')
    for brandName in brandPages:
        try:
            if ( brandName.text != "" and brandName.text != "info@bike-data.com"):
                bicycles[brandName.text] = {}
        except:
            print("          -- err in "+brandName)
except:
    print("Error -- finding brand pages")
else:
    print("Success\n")

# # download brand pages
# os.mkdir("./HTMLFiles")
# print("Start   --  Downloading brand pages")
# counter = 1
# counterMax = len(bicycles)
# try:
#     for i in bicycles:
#         percent = round(counter/counterMax*100)
#         print("====== Downloading "+ i +" --- " + str(counter) + " of " + str(counterMax) + " ==== " + str(percent) +" percent complete                                                    ", end='\r')
#         counter+=1
#         try:
#             url = "http://bike-data.com/en/" + i
#             wget.download(url, out="./HTMLFiles/"+i+".html")
#         except:
#             print("          -- err in "+i)
# except:
#     print("Error -- downloading brand pages")
# else:
#     print("Success\n")
    

# find model pages for every brand
print("Start   -- finding model pages")
for i in bicycles:
    location = "./HTMLFiles/"+i+".html"
    brandFile = open(location, "r")
    try:
        brandPage = BeautifulSoup(brandFile, "html.parser")
    except:
        print("        -- err while parsing "+ i +".html")
    else:
        tableElements = brandPage.findAll("td")
        bicycles[i] = []
        for element in tableElements:
            bicycles[i].append(
                {
                    "name":element.find("a").text,
                    "link":element.find("a")["href"],
                }
            )
print("Success\n")

# # download model pages
# print("Start   -- downloading model pages")
# brandCounter = 1
# brandMax = len(bicycles)
# for brand in bicycles:
#     os.mkdir("./HTMLFiles/" + brand)
#     location = "./HTMLFiles/"+brand+"/"
    
#     modelCounter = 1
#     modelMax = len(bicycles[brand])
#     brandPercent = round(brandCounter/brandMax*100)
#     print("\n====== Downloading "+ brand +"  ---  "+ str(brandCounter) + " of " + str(brandMax) + " ==== " + str(brandPercent) +" percent complete")
#     for model in bicycles[brand]:
#         url = "http://bike-data.com"+model['link']
#         name = model['name']+".html"
#         modelPercent = round(modelCounter/modelMax*100) 
#         print("============== Downloading "+ str(modelCounter) + " of "+ str(modelMax) + " ======= " + str(modelPercent) + " percent completed                                                                  ", end='\r')
#         try:
#             wget.download(url, out=location+name+".html")
#         except:
#             print("          -- err in "+model['link'])
#         modelCounter+=1

#     brandCounter+=1
# print("Success\n")


howMany = 15
divided = []
for i in range(howMany):
    divided.append([])
counter = 0
for i in bicycles:
    for j in bicycles[i]:
        which = counter%howMany
        divided[which].append({
            "name":i+"--"+j['name'],
            "link":j['link']
        })
        counter+=1

toFile = "import wget\nimport os\nlink="
forFile = """
for i in link:
    outName = i['name']+'.html'
    outName = outName.replace('/','')
    outName = outName.replace(' ','_')
    try:
        wget.download('http://bike-data.com'+i['link'],out=outName)
    except:
        print("err while downloading"+i['link'])
"""

counter = 0
for i in divided:
    endofend = toFile + str(i) + forFile
    fileName = "downLink"+str(counter)+".py"
    counter+=1
    create = open(fileName, 'w')
    create.write(endofend)


shFile = open("downloadAll.sh","w")
shString = "#!/usr/bin/env bash\n"
counter = 0
for i in divided:
    shString+="python3 ./downLink"+str(counter)+".py &\n"
    counter+=1
shFile.write(shString)