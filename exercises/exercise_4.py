# Your solution to Exercise 4
grade = int(input("Grade = "))
if grade in [1,2,3]:
  level = "initial"
elif grade in [4,5,6]:
  level = "average"
elif grade in [7,8,9]:
  level = "sufficient"
elif grade in [10,11,12]:
  level = "high"
else:
  level = 'absent'
print("Level is",level)
