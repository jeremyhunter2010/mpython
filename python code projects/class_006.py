'''
Coin Flip Simulation
'''
import random

print("How many times should we flip the coin")
_number = input()

if int(_number) < 1 :
  print("You cannot flip less than once")
  exit()

 
for i in range(0, int(_number), 1):
 n = random.randint(0,1)
 if n == 0:
   print("Tail")
 else:
   print("Head")