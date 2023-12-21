print("---Let's play rock, paper, scissors---")
print("You are player one (p1)")
p1 = int(input("Please press 1 for rock, 2 for paper, 3 for scissors-->> ").strip())
import random
p2 = random.randint(1,3)

def rps(p1, p2):
  if (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2) or (p1 == 1 and p2 == 3):
    print("p1 wins")
  elif (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 3) or (p1 == 3 and p2 == 1):
    print("p2 wins")
  else:
    print("Draw")



rps(p1, p2)