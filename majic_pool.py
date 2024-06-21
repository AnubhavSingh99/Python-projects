# Write code below 💖
import random
a1='Yes - definitely.'
a2='It is decidedly so.'
a3='Without a doubt'
a4='Reply hazy, try again'
a5='Ask again later'
a6='Better not tell you now'
a7='My sources say no'
a8='Outlook not so good'
a9='Very doubtful'
q=input("Ask any YES or NO type question\n")
num = random.randint(1, 9)
if num == 1:
  print(a1)
elif num == 2:
  print(a2)
elif num == 3:
  print(a3)
elif num == 4:
  print(a4)
elif num == 5:
  print(a5)
elif num == 6:
  print(a6)
elif num == 7:
  print(a7)
elif num == 8:
  print(a8)
else:
  print(a9)

