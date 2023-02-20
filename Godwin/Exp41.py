import csv
with open("dep (1).csv","r")as f:
    r=csv.reader(f)
    for i in r:
        print(i)