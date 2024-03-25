# Your solution to Exercise 5

from math import sqrt
def roots(a,b,c):
  if [a,b,c] == [0,0,0]:
    print("Infinite roots")
  elif b**2 - 4*a*c < 0:
    print('No roots')
  elif b**2 - 4*a*c == 0:
    print(
      round(
        (-b + sqrt((b**2) - (4*a*c)))/(2*a)
        ,2)
    )
  else:
    r1 = (-b + sqrt((b**2) - (4*a*c)))/(2*a)
    r2 = (-b - sqrt((b**2) - (4*a*c)))/(2*a)
    print(round(r1,2),round(r2,2))


roots(8,4,2)
roots(3.6,10,-3)
roots(2,4,2)
roots(1,2,3)
roots(0,0,0)
