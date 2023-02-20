class first:
    a=int(input("Enter the first number: "))
    def second(self):
        print(self.a)
class second:
    b=int(input("Enter the second number: "))
    def second(self):
        print(self.b)
class third:
    c=int(input("Enter the third number: "))
    def third(self):
        print(self.c)
class compare(first,second,third):
    def num(self):
        print()
p=compare()
if p.a>p.b and p.c:
    print("First number is greater.",p.a)
elif p.b>p.a and p.b>p.c:
    print("Second number is greater.",p.b)
else:
    print("Third number is greater.",p.c)
