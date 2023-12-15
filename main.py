import random 

input("Heads or Tails? Type Heads or Tails. ")

randomInteger = random.randint(0,1)

if randomInteger == 1:
  print("Heads")
else:
  print("Tails")