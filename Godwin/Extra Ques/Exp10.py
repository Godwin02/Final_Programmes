sum=lambda x,y:x+y
n=int(input("Enter the limit of the series"))
print("The fibonacci series upto ",n,"are")
a=0
b=1
if(n==0):
    print(0)
elif(n==1):
    print(0,1)
else:
    print(a)
    print(b)
    for i in range (2,n):
        c=sum(a,b)
        print(c)
        a=b
        b=c