class rectangle():
    def __init__(self):
        self._hour = int(input("Enter the Length:"))
        self._minute = int(input("Enter the Breadth:"))
        self.second = self._hour * self._minute
    def greaterThan(self,rectangle):
        if self.second < rectangle.second:
            print("Area of Rectangle 1 is Greater")
        else:
            print("Area of Rectangle 2 is Greater")

print("Rectangle 1:")
r1 = rectangle()
print("Rectangle 2:")
r2 = rectangle()
print("Comparing Areas:-")
r2.greaterThan(r1)