# Your solution to Exercise 2
def ageGroup(y):
  if y<1:
    group = "an infant."
  elif y<13:
    group = "a child."
  elif y<20:
    group = "a teenager."
  else:
    group = "an adult."
  print("You are",group)

ageGroup(3)
ageGroup(14)
ageGroup(25)
