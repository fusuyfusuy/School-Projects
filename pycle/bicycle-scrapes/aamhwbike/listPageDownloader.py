import os
import wget
from bs4 import BeautifulSoup

urls = [
    'https://www.mhw-bike.com/bikes/mountainbikes-hardtail/', # 5
    'https://www.mhw-bike.com/bikes/mountainbikes-fully/', # 3
    'https://www.mhw-bike.com/bikes/citybikes/', # 4
    'https://www.mhw-bike.com/bikes/freestyle/', # 1
    'https://www.mhw-bike.com/bikes/kid-bikes/', # 4 
    'https://www.mhw-bike.com/bikes/road-bikes/']  #3


mountainHard = urls[0]
mountainFull = urls[1]
city = urls[2]
kid = urls[3]
free = urls[4]
road = urls[5]

for i in range(5):
    wget.download(mountainHard+'?p='+str(i+1), out='listPages/moountainHard'+str(i+1))
    
for i in range(3):
    wget.download(mountainFull+'?p='+str(i+1), out='listPages/mountainFull'+str(i+1))

for i in range(4):
    wget.download(city+'?p='+str(i+1), out='listPages/city'+str(i+1))

for i in range(1):
    wget.download(kid+'?p='+str(i+1), out='listPages/kid'+str(i+1))

for i in range(4):
    wget.download(free+'?p='+str(i+1), out='listPages/free'+str(i+1))

for i in range(3):
    wget.download(road+'?p='+str(i+1), out='listPages/road'+str(i+1))