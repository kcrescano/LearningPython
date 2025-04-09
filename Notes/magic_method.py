class Sun:
  n = 0  # number of instances of this class

  # __init__(): also a magic method
  def __new__(cls):
    if cls.n == 0:
      cls.n += 1
      return object.__new__(cls)  # create new object of the class

class Transaction:
  def __init__(self, number, funds, status="active"):
    self.number = number
    self.funds = funds
    self.status = status
  
  def __repr__(self):
    return "Transaction({}, {})".format(self.number, self.funds)
    # Transaction 000001 for 9999.999 (active)
  def __str__(self):
    return "Transaction {} for {} ({})".format(self.number, self.funds, self.status)
