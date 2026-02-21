class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.age)
print(dog1.species)

print("===================================================")

class Animal:
    def __init__(self, name):
        self.name = name
        print(name)

    def info(self,value1):
        print("Animal name:", value1)
    def test(self,value):
        print("Test name:", value)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info("end")      # Inherited method
d.test("testing")
d.sound()


print("===================================================")

# Parent Class: Animal
class Animal:
    def __init__(self, name ):
        self.name = name


    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def details(self):
        print("bread name : ", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method