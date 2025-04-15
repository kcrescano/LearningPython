class River:
  all_rivers = []  # class attribute

  # constructor
  def __init__(self, name, length):
    self.name = name  # instance attribute
    self.length = length
    River.all_rivers.append(self)

  # class method
  def get_info(self):
    print("The length of the {0} is {1} km".format(self.name, self.length))

# class intances
volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# self.method()
volga.get_info()
# class.method(self)
River.get_info(volga)
#**************************************************************************
# parent class
class Animal:
    def __init__(self, name):
        self.name = name

# child class
class Dog(Animal):
    pass
  
cow = Animal("Bessie")  # instance of Animal
corgi = Dog("Baxter")   # instance of Dog

print(type(cow) == Animal)  # True
print(type(cow) == Dog)     # False

print(isinstance(cow, Animal))    # True
print(isinstance(corgi, Animal))  # True
print(isinstance(cow, Dog))    # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
print(issubclass(corgi, Dog))   # TypeError
print(issubclass(Dog, (Animal, object)))  # True
