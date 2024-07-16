#  Imagine you are maintaining a list of tasks for your day. Write a Python script to perform the following tasks in order, demonstrating the use of different list methods:
# 
# Add three tasks to your list. (Tasks: "task1", "task2", "task3")
# Create a backup copy of the current list of tasks.
# Add three more tasks to your list. (Tasks: "task4", "task5", "task6")
# Insert a high-priority task at the beginning of the list. (Task: "urgent task")
# Find and print the position of "task4" in the list.
# Count and print how many times "task2" appears in the list.
# Remove "task3" from the list.
# Complete and remove the last task from the list, and print the task that was completed.
# Reverse the order of the list.
# Sort the list alphabetically.
# Clear all the tasks from the list and print the empty list.




tasks = []
tasks.append("task1")
tasks.append("task2")
tasks.append("task3")
print("After adding task1, task2, task3:", tasks)

tasks_backup = tasks.copy()
print("Backup of the task list:", tasks_backup)

tasks.extend(["task4", "task5", "task6"])
print("After adding task4, task5, task6:", tasks)

tasks.insert(0, "urgent task")
print("After adding 'urgent task' at the beginning:", tasks)

index_of_task4 = tasks.index("task4")
print("Position of 'task4' in the list:", index_of_task4)

count_of_task2 = tasks.count("task2")
print("Count of 'task2' in the list:", count_of_task2)

tasks.remove("task3")
print("After removing 'task3':", tasks)

completed_task = tasks.pop()
print("Completed task:", completed_task)
print("After completing the last task:", tasks)

tasks.reverse()
print("After reversing the list:", tasks)

tasks.sort()
print("After sorting the list:", tasks)

tasks.clear()
print("After clearing the list:", tasks)



