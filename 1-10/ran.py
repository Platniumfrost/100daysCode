import random

def cointoss():
    rand_i = random.randint(0,1)
    outcomes = ["Heads", "Tails"]
    return outcomes[rand_i]

t1 = cointoss()
print(t1)


random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")


def random_name():
    rand_i = random.randint(0,4)
    names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
    return names[rand_i]

t1 = random_name()
print(t1)

