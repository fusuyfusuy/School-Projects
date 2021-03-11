import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url = 'https://www.chainreactioncycles.com/tr/en/bikes?sort=az&page=' # 9 sayfa

for i in range(9):
    try:
        req = Request(url+str(i+1), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        print('error in '+str(i+1))
    else:
        newFile = open('list'+str(i+1)+'.html','wb')
        newFile.write(webpage)

