class Publisher():
    def __init__(self,pubname):
        self.pubname =pubname
    def display(self):
        print("Publisher :", self.pubname)

class Book(Publisher):
    def __init__(self,pubname):
        Publisher.__init__(self,pubname)

    def bookdetails(self):
        self.title= input("Book Name :")
        self.author = input("Book Author :")

    def display(self):
        print("Title :", self.title)
        print("Authur :", self.author)

class Python(Book):
    def __init__(self,pubname):
        Book.__init__(self,pubname)
    def moredetails(self):
        self._price = int(input("Book Price :"))
        self._pages = int(input("Book Pages :"))
    def display(self):
        print("Publisher :",self.pubname)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self._price)
        print("Pages :",self._pages)

obj = Python("Publisher")
obj.bookdetails()
obj.moredetails()
print("___________________________________________")
obj.display()
