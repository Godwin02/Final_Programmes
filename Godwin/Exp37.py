class time():
    def __init__(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def add(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=time(2,10,5)
o2=time(4,5,10)
print((o2).add(o1))
