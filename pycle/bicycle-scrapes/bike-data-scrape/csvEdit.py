import os
import csv

bicycles = []
with open('bicycles.csv', 'r') as file:
    reader = csv.reader(file)
    counter = 0
    for row in reader:
        if(counter == 0):
            print(row)
        counter +=1