f=open("demo.txt","r")
num=0
for line in f:
    words=line.split()
    num +=len(words)
print("Number of Words")
print(num)
f.close()