colorlist1=[]
n=int(input("Eneter the size of the colorlsit1:"))
print("Enter the colors:",end=" " )
for i in range(0,n):
    ele=input()
    colorlist1.append(ele)
print(colorlist1)
colorlist2=[]
n=int(input("Enter the size of the colorlist2:"))
print("Enter the colors: ",end=" ")
for i in range(0,n):
    ele=input()
    colorlist2.append(ele)
print(colorlist2)
a=set(colorlist1)
b=set(colorlist2)
m=a.difference(b)
n=list(m)
print(n)
