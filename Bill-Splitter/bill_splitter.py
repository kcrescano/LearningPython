import random

friend_count = int(input('Enter the number of friends joining (including you):'))
friends = {input(): 0 for _ in range(friend_count)}

if friend_count > 0:
  total_bill = float(input('Enter the total bill value:'))
  lucky_friend = None
  
  lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
  if lucky_feature == 'Yes':
    lucky_friend = random.choice(list(friends.keys()))
    total_bill /= len(friends) - 1
    print(f'{lucky_friend} is the lucky one!')
  else:
    print('No one is going to be lucky')
    total_bill /= len(friends)
    friends = dict.fromkeys(friends, round(total_bill, 2))
    
  if lucky_friend:
    friends[lucky_friend] = 0
      
print(friends if friends else 'No one is joining for the party')
