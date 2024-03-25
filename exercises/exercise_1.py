# Your solution to Exercise 1
def olderOf(A,T):
  if A==T:
    print("Alex and Tatyana are of the same age.")
  else:
    print(["Alex","Tatyana",][A<T],"is the eldest.")

olderOf(17,22)
olderOf(25,25)
olderOf(30,28)
