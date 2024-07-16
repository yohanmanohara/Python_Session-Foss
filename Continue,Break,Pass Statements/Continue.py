# Q: Get a count of the students who’s grade is above 60 (use continue statement to skip others)


grades = [70, 55, 85, 40, 90]
count = 0
for grade in grades:
 if grade < 60:
  continue
count += 1
print("The number of students who passed is", count)


