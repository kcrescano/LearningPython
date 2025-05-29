# write your code here
import random

print('Enter the number of friends joining (including you):')
users = {input(): 0  for _ in range(int(input()))}

if users:
    print('Enter the total bill value:')
    bill = float(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if input() == 'Yes':
        share = bill / (len(users) - 1)
        lucky = random.choice(list(users.keys()))
        print(f'{lucky} is the lucky one!')
    else:
        share = bill / len(users)  
        
    share = int(share) if share.is_integer() else round(share, 2)
    users.update({user: share for user in users})
    
    try:
        if lucky:
            users[lucky] = 0
    except NameError:
        print('No one is going to be lucky')

print(users or "No one is joining for the party")
