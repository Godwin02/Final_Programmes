x=input("Enter the string: ")
print(x)
if x[-3:]=="ing":
    x=x.replace(x[-3:],"ly")
else:
    x=x+"ing"
print(x)