class first():
    def __init__(self):
        self.a = int(input("Enter the first number: "))
class second(first):
    def __init__(self):
      first.__init__(self)
      self.b = int(input("Enter the second number: "))
class third():
    def __init__(self):
        self.c= int(input("Enter the third number: "))
class compare(second,third):
    def __init__(self):
        second.__init__(self)
        third.__init__(self)
        if self.a>self.b and self.a>self.c:
            print("First number is greater.",self.a)
        elif self.b>self.a and self.b>self.c:
            print("Second number is greater.",self.b)
        else:
            print("Third number is greater.",self.c)
p=compare()
