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
