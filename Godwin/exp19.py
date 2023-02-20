l=[]
n=int(input("Enter the range:"))
print("Enter the elements:")
for i in range(0,n):
    ele=int(input())
    if (ele%2!=0):
        l.append(ele)
print(l)