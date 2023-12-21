import random

num = random.randint(1,50)

rights = 5
print("Let's play guessing game!!!")
print("What is the number in my mind? From 1 to 50")
print(f"You have {rights} rights")

while rights > 0:
  guess = int(input("Please enter your guess: "))
  rights -= 1  
  if guess == num:
    print("<<<Congratulations!>>>")
    break
  elif guess > num and rights >= 1:
    print(f"Please lower your guess. You have {rights} rights")
  elif guess < num and rights >= 1:
    print(f"Please increase your guess. You have {rights} rights")

else:
  print(f"<<<GAME OVER>>> The number was {num}")


if rights == 4:
  print("Point=100. You must be a mind reader!")
elif rights == 3:
  print("Point=80. Well done!!!")
elif rights == 2:
  print("Point=60. You are on the ball")
elif rights == 1:
  print("Point=40. Not bad!")
elif rights == 0 and guess == num:
  print("Point=20. Better late than never!")
else:
  print("Hang in there!")
