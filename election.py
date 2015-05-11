from random import randint

for i in range(10000):
  rolls = randint(1,100)
  wins=0 
  if rolls <= 87:
    wins=wins+1
  if rolls <= 65:
    wins=wins+1
  if rolls <= 17: 
    wins=wins+1
  if wins >=2: 
    print "you win the election." 
  if wins<=2"
  print "you lost the election."
  
