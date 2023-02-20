list1=[]
list2=[]
n=int(input("Enter the number of Words"))
for i in range (0,n):
    ele=input()
    list2.append(ele)
print(list2)
for i in list2:
    for j in i:
        values=ord(j)
        list1.append(values)
print("The ordinal values of the element is:",list1)