# Your solution to Exercise 6
def furtherfromOrigin(A1,A2,B1,B2):
  print(A1**2+A2**2, B1**2+B2**2)
  if A1**2+A2**2 == B1**2+B2**2:
    print("Distances are the same")
  else:
    print("AB"[A1**2+A2**2 < B1**2+B2**2], "is further from the origin.")

furtherfromOrigin(1,2,3,4)
furtherfromOrigin(1,2,2,4)
furtherfromOrigin(1,2,0,0)
