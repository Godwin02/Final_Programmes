class myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
            print("Addition")
            print(self.x+self.y)
            print("Substraction")
            print(self.x-self.y)
            print("Multiplication")
            print(self.x*self.y)
            print("Division")
            print(self.x/self.y)
p=myclass(10,5)
print(p.x)
print(p.y)
print("Mathematical operations on these numbers are: ")
p.show()
print(myclass)
