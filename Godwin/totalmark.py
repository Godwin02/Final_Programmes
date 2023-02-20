class student():
    def __init__(self):
        self.Name=str(input("Enter the Name of Student:"))
    def marks(self):
        self.subject1 = int(input("Enter the Marks 1:"))
        self.subject2 = int(input("Enter the Marks 2:"))
        self.subject3 = int(input("Enter the Marks 3:"))
        self.subject4 = int(input("Enter the Marks 4:"))
    def Total(self):
        total = self.subject1+self.subject2+self.subject3+self.subject4
        return total

array = []
n = int(input("Enter the Number of Students Information to be Entered:"))
for i in range(n):
    array.append(student())
    array[i].marks()

for i in range(n):
    print("Name:",array[i].Name)
    print("Total:",array[i].Total())