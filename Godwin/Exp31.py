n=int(input("Enter the size: "))
print("The given diagram is: ")
for i in range (0,n+1):
    for j in range(i):
        print("*",end=" ")
    print(" ")
for i in range(n-1,0,-1):
    for j in range (i):
        print("*",end=" ")
    print(" ")


