import math

def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {round_up_cans} cans of paint.")

print("Hi! I will help you with your wall painting job!")
test_h = int(input("how tall is your wall?>"))
test_w = int(input("how wide is your wall?"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)