a=[2,3,4,6,7]
b=[8,5,6,7,8]
print(len(a))
print(len(b))
if len(a)==len(b):
    print("same length")
else:
    print("not same length")
sum1=sum(a)
sum2=sum(b)
if sum1==sum2:
    print("same value")
else:
    print("The sum is not same")
a=print(set(a)&set(b))
if a==0:
    print("not occuring")
else:
    print("same value are occuring")