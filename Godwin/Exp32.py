n=int(input("enter a digit"))
for i in range(0,n+1):
    for j in range(1,i+1):
        j=i*j
        print(j,end=" ")
    print("\r")