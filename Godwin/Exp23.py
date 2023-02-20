dict={}
string1=input("Enter the string: ")
for j in string1:
    if j in dict:
        dict[j]+=1
    else:
        dict[j]=1
print("Character frequency;")
for m,n in dict.items():
    print(m,n)