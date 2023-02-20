class first:
    def __init__(self,a):
        self.a=int(input("Enter the first number: "))
class second(first):
    def __init__(self,b):
        first.__init__(self, b)
        self.b=int(input("Enter the second number: "))

class third(second):
    def __init__(self,c):
        second.__init__(self, c)
        self.c=int(input("Enter the third number: "))

p=third("")
if p.a>p.b and p.a>p.c:
    print("First number is greatest one.",p.a)
elif p.b>p.a and p.b>p.c:
    print("Second number is greatest one.",p.b)
else:
    print("Third number is greatest one.",p.c)
