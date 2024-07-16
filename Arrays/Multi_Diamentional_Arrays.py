# Write a Python program that takes this 2D array as input and prints it. 
# The function should also count and return the total number of elements in the entire array


seating_chart = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve", "Frank"],
    ["Grace", "Heidi", "Ivan"]
]
total_students = 0
for row in seating_chart:
    print(row , "\n")
    total_students += len(row)

print(seating_chart)
print(f"The total number of students in the classroom is {total_students}.")
