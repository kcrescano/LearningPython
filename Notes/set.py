empty_set = set()

flowers = {'rose', 'lilac', 'daisy'}
# the order is not preserved
print(flowers)  # {'daisy', 'lilac', 'rose'}  
letters = set('philharmonic')
print(letters)  # {'h', 'r', 'i', 'c', 'o', 'l', 'a', 'p', 'm', 'n'}

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)  # True

nums = {1, 2, 2, 3}
print(1 in nums, 4 not in nums)  # True True

nums = {1, 2, 2, 3}
nums.add(5)
print(nums)  # {1, 2, 3, 5}

more_nums = {6, 7}
nums.update(more_nums)
print(nums)  # {1, 2, 3, 5, 6, 7}
 
# we can also add a list
text = ['how', 'are', 'you']
nums.update(text)
print(nums)  # {'you', 1, 2, 3, 5, 6, 7, 'are', 'how'}
 
# or a string
word = 'hello'
nums.add(word)
print(nums)  # {1, 2, 3, 'how', 5, 6, 7, 'hello', 'you', 'are'}

nums.remove(2)
print(nums)  # {1, 3, 5}

empty_set = set()
empty_set.discard(2)  # nothing happened
empty_set.remove(2)   # KeyError: 2

nums = {1, 2, 2, 3}
nums.pop()  # random
print(nums)  # {2, 3}

nums.clear()  # remove all

# frozenset is immutable and can be part of list and can be a key in dict
some_frozenset = frozenset(text)
nested_text.add(some_frozenset)
print(nested_text)  # {'!', frozenset({'world', 'hello'})}
