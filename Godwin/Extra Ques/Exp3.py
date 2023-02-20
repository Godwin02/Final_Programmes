f=open("demo.txt","r")
content=f.readlines()
res=[]
for i in content:
    res.append(i.replace("\n",""""""))
print(res)
f.close()