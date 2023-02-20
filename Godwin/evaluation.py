x=[]
n=int(input("Enter the size of the series: "))
print("Enter the numbers: ",end=" ")
a=0
b=1
c=1
i=0
while i<n-2:
    if a==0:
        print(a)
        x.append(a)
        x.append(c)
    c=a+b
    a=b
    b=c
    x.append(c)
    i=i+1
print(x)
for j in (x):
    if j%12==0:
     print(j,end=" ")