# Your solution to Exercise 3
def roulette(i):
  if i in range(1,11):
    if i%2:
      print("Red")
    else:
      print("Black")
  elif i in range(11,19):
    if not i%2:
      print("Red")
    else:
      print("Black")
  elif i in range(19,29):
    if i%2:
      print("Red")
    else:
      print("Black")
  elif i in range(29,37):
    if not i%2:
      print("Red")
    else:
      print("Black")
  elif i == 0:
    print("Green")
  else:
    print("The bet will not play!")

roulette(24)
roulette(34)
roulette(0)
roulette(37)
