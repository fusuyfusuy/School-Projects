import os 
from urllib.request import Request, urlopen


bmx = 'https://www.chainreactioncycles.com/bmx-bikes?sort=az&page=' # 2
cross = 'https://www.chainreactioncycles.com/cyclo-cross-bikes?sort=az&page=' # 1
electric = 'https://www.chainreactioncycles.com/electric-bikes?sort=az&page=' # 1 
folding = 'https://www.chainreactioncycles.com/folding-bikes?sort=az&page=' # 1 
hybrid = 'https://www.chainreactioncycles.com/hybrid-city-bikes?sort=az&page=' # 2
kid = 'https://www.chainreactioncycles.com/kids-bikes?sort=az&page=' # 1
mountain = 'https://www.chainreactioncycles.com/mountain-bikes?sort=az&page=' # 4
road = 'https://www.chainreactioncycles.com/road-bikes?sort=az&page=' # 2 
tt = 'https://www.chainreactioncycles.com/tt-bikes?sort=az&page=' # 1
os.mkdir('listPages/bmx')
os.mkdir('listPages/cross')
os.mkdir('listPages/electric')
os.mkdir('listPages/folding')
os.mkdir('listPages/hybrid')
os.mkdir('listPages/kid')
os.mkdir('listPages/mountain')
os.mkdir('listPages/road')
os.mkdir('listPages/tt')

for i in range(1):
    url = tt
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/tt/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(2):
    url = road
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/road/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(4):
    url = mountain
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/mountain/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(1):
    url = kid
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/kid/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(2):
    url = hybrid
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/hybrid/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(1):
    url = folding
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/folding/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(1):
    url = electric
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/electric/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(1):
    url = cross
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/cross/'+str(i+1)+'.html','wb')
        newFile.write(webpage)

for i in range(2):
    url = bmx
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
 
        newFile = open('listPages/bmx/'+str(i+1)+'.html','wb')
        newFile.write(webpage)
