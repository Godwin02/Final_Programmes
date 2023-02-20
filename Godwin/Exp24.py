string=input("Enter the line:")
str=string.split(' ')
dict={}
for j in str:
    if j in dict:
        dict[j]+=1
    else:
        dict[j]=1
print("occurance")
for m,n in dict.items():
    print(m,n)