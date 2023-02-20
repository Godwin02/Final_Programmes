f=open("Extra Ques/demo.txt", "r")
f1=open("Odd.txt","w")
content=f.readlines()
for i in range(0,len(content)):
    if i%2==1:
        f1.write(content[i])
    else:
        pass
f1.close()
f.close()
f=open("Odd.txt","r")
print("Odd lines are:  ",f.read())