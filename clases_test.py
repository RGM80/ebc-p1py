
class Dog:
    def __init__(self, name, size, color, race):
        self.name = name
        self.size = size
        self.color = color
        self.race = race

    def printInfo(self):
        print(self.name, self.size, self.color, self.race)

dog = Dog("firulais", 15, "cafe", "pastor aleman")
dog1 = Dog("firula", 10, "blanco", "pastor")

dog. printInfo()
dog1. printInfo()



