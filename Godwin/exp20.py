n=int(input("Enter the size of series:"))
a=0
b=1
c=1
for i in range(1,n):
    if a==0:
        print(a,end=" ")
    print(c, end=" ")
    c=a+b
    a=b
    b=c
