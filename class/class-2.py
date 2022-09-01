class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printName(self):
        print(self.name, self.age)


class Student(Parent):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    
    def printName(self):
        print(self.name, self.age, self.year)

p1 = Parent("jphn", 21)
p1.printName()
p2 = Student("smith", 32, 1982)
p2.printName()