 # Printing Star
#for row in range(8):
#     for col in range(6):
#         print('*', end='')
#     print()
# 
 
 
 
 # This program displays a rectangular pattern
 # of asterisks.
#rows = int(input('How many rows? '))
#cols = int(input('How many columns? '))
#
#for r in range(rows):
#    for c in range(cols):
#        print('*', end='')
#    print()

# This program displays a triangle pattern.
BASE_SIZE = 8

for r in range(BASE_SIZE):
    for c in range(r + 1):
         print('*', end='')
    print()

# This program displays a stair–step pattern
NUM_STEPS = 6

for r in range(NUM_STEPS):
  for c in range(r): # r = 0,r=1
      print('&', end='')
  print('#')