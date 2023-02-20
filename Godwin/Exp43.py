import csv
c_column=['ID','Name','Age']
dict_data=[{'ID':1,'Name':'Raoof','Age':15},
           {'ID':2,'Name':'Abhinamol','Age':16},
           {'ID':3,'Name':'Abhinand','Age':14},
           {'ID':4,'Name':'Abhiramy','Age':18},
           {'ID':5,'Name':'Ajel','Age':17},
           {'ID':6,'Name':'Akash','Age':14},
           {'ID':7,'Name':'Akhil','Age':16},
           {'ID':8,'Name':'Akhila','Age':14},
           {'ID':9,'Name':'Akku','Age':17},
           {'ID':10,'Name':'Aleena','Age':13}]
try:
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_column)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("Input/Output Error")
d=csv.DictReader(open("name.csv"))
print("The csv file output is:")
for i in d:
    print(i)
#with open("file.csv",newline='')as dict_data:
    #d=csv.writer(dict_data)
#with open("file.csv","r")as f:
 #   r = csv.reader(f)
  #  for i in r:
   #     print(i)