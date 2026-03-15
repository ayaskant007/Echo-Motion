class Animals:
    
    def show(self):
        print("These are animals")

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("Woof! Woof!")

a = Animals()
a.show()
b = Pets()
# b.show()
c = Dog()
c.bark()