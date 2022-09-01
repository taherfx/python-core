class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printName(self):
        print(self.name, self.age)


p1 = myClass("jphn", 21)
p1.printName()