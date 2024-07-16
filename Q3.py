
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


