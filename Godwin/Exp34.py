class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
            return self.length*self.breadth
    def perimeter(self):
            return (2*(self.length+self.breadth))
l=int(input("Enter the length="))
b=int(input("Enter the breadth="))
o=rectangle(l,b)
x=o.area()
y=o.perimeter()
print("Area=",x)
print("Perimeter=",y)

l1=int(input("Enter the length="))
b1=int(input("Enter the breadth="))
o1=rectangle(l1,b1)
z1=o1.area()
print("Area=",z1)
if(x>z1):
    print("1st rectangle is grater than 2nd rectangle")
if(x==z1):
    print("Both their area are same")
if(x<z1):
    print("2nd rectangle is grater than 1st .")