import random


choice = input('Would you like one flip? or 10?:  ' )

sequence = [0,1,2,3,4,5,6,7,8,9]
flips = []

def flips_coin(sequence):
    for val in sequence:
        flip = random.randrange(1,10)
        if flip >= 5:
            flips.append('heads')
        else:
            flips.append('tails')

flips_coin(sequence)

if choice == '1':
  result = random.choice(flips)
elif choice == '10':
  result = flips
else:
  result = 'Invalid choice, run again...'

print(result)