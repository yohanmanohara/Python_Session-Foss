# Q: write a program to create student mark grading system using for loop


marks = [85, 92, 78, 60, 95]

for mark in marks:
 if mark >= 90:
  print(f"mark {mark}: Grade A")
 elif mark >= 80:
  print(f"mark {mark}: Grade B")
 elif mark >= 70:
  print(f"mark {mark}: Grade C")
 else:
  print(f"mark {mark}: Grade F")


