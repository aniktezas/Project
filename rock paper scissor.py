import random as rd
k=['Rock','Paper','Scissor']
l=input(f'What is your choice {k}?\n')
j=rd.choice(k)
print(j)
if l in k:
    if l==j:
        print("It's a tie.")
    elif (l==k[0] and j==k[1]) or (l==k[1] and j==k[2]) or (l==k[2] and j==k[0]):
        print('Computer win')
    else:
        print('You Win')
else:
    print('Please input a valid option.')