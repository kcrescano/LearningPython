# list
list_ = [] or list() # empty list
list_ = list("abcde") # is the same as
list_ = ["a", "b", "c", "d", "e"]
# split function to make a list
list_ = "a b c d e".split() # only with spaces as default
# len() can be use to get how many element a list have (or any iterable) 

list_ = [1, 2, 3, 4, 5]
# adding elements
list_.append(1)
list_.insert(0, 0) # index, value
list_.extend([10, 20, 30])
list_ += list("abcde")
# removing elements
list_.remove("a") # only the first occurance
del list_[1] # using index
list_.pop() # last element like stack
list_.pop(2) # using index



# list comprehension
list_ = [elem for elem in input()] # list of str
list_ = [int(elem) for elem in input()] # list of int
