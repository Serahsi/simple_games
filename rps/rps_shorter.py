import random

a = random.randint(0, 2)
b = random.randint(0, 2)

if a == b:
    print("draw game")
elif a == (b + 1) % 3:
    print("winner is B")
else:
    print("winner is A")