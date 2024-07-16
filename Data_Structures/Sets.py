# You have two sets representing students in two different classes: class_a = {"John", "Sara", "Tom"} and class_b = {"Tom", "Amy", "Eve"}.
# Write a line of code to find the students who are in both classes


class_a = {"John", "Sara", "Tom"}
class_b = {"Tom", "Amy", "Eve"}
common_students = class_a.intersection(class_b)
print(common_students)