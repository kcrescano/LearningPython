# for loop

# for "each" 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue # skip to next iteration
  print(x)

# for loop with range
for x in range(6):
  if x == 3:
    break # breaks the loop
  print(x)
else:
  print("Finally finished!")
# If the loop breaks, the else block is not executed.

# while loop
i = 1
while i < 6:
  print(i)
  i += 1
# else, continue and break works the same with while loop
