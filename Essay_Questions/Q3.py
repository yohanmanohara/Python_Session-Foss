# 1. Input 10 numbers and output the number of positive, number of negative, number of zeros.
# 2. Input Marks of 10 students and output the maximum, minimum and average marks.
# 3. Input price of 10 items and display the average value of an Item, number of items which the price is greater than 200.
# 4. Input the Employee No and the Basic Salary of the Employees in an organisation, ending with the
#       dummy value -999 for Employee No and count the number Employees whose Basic Salary > = 5000.
# 5. Input Employee Number and Hours worked by employees to display the following:
#       • Employee Number, Over Time Payment, and the percentage of employees whose Over Time Payment exceed Rs. 4000/-.
#       • The user should input -999 as Employee Number to end the program, and the normal Over Time
# Rate is Rs. 150 per hour and Rs. 200 per hour for hours in excess of 40.





# Task 1: Counting positives, negatives, and zeros

numbers = []
for i in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

positives = sum(1 for n in numbers if n > 0)
negatives = sum(1 for n in numbers if n < 0)
zeros = sum(1 for n in numbers if n == 0)

print(f"Number of positive numbers: {positives}")
print(f"Number of negative numbers: {negatives}")
print(f"Number of zeros: {zeros}")



# Task 2: Maximum, minimum, and average marks

marks = []
for i in range(10):
    mark = float(input("Enter marks of student: "))
    marks.append(mark)

maximum = max(marks)
minimum = min(marks)
average = sum(marks) / len(marks)

print(f"Maximum marks: {maximum}")
print(f"Minimum marks: {minimum}")
print(f"Average marks: {average:.2f}")


# Task 3: Average price and count of items with price greater than 200

prices = []
for i in range(10):
    price = float(input("Enter price of item: "))
    prices.append(price)

average_price = sum(prices) / len(prices)
count_greater_200 = sum(1 for p in prices if p > 200)

print(f"Average price: {average_price:.2f}")
print(f"Number of items with price greater than 200: {count_greater_200}")



# Task 4: Count employees with Basic Salary >= 5000

count = 0

while True:
    emp_no = int(input("Enter Employee Number (-999 to end): "))
    if emp_no == -999:
        break
    basic_salary = float(input("Enter Basic Salary: "))
    if basic_salary >= 5000:
        count += 1

print(f"Number of employees with Basic Salary >= 5000: {count}")


# Task 5: Over Time Payment and percentage of high Overtime Payment employees

overtime_rate_normal = 150
overtime_rate_excess = 200
employee_data = []

while True:
    emp_no = int(input("Enter Employee Number (-999 to end): "))
    if emp_no == -999:
        break
    hours_worked = float(input("Enter Hours Worked: "))
    
    if hours_worked <= 40:
        overtime_payment = hours_worked * overtime_rate_normal
    else:
        overtime_payment = 40 * overtime_rate_normal + (hours_worked - 40) * overtime_rate_excess

    employee_data.append((emp_no, overtime_payment))

high_overtime_count = sum(1 for _, payment in employee_data if payment > 4000)
total_employees = len(employee_data)
high_overtime_percentage = (high_overtime_count / total_employees) * 100 if total_employees > 0 else 0

print("Employee Number | Over Time Payment")
for emp_no, payment in employee_data:
    print(f"{emp_no} | {payment:.2f}")

print(f"Percentage of employees with Over Time Payment exceeding Rs. 4000: {high_overtime_percentage:.2f}%")
