# Q: Get the temperature as a user input each day and calculate the average temperature of the week using a single dimensional array

for i in range(7):
    temperatures = []
    temperatures.append(float(input(f"Enter the temperature for day {i + 1}: ")))

average_temperature = sum(temperatures) / len(temperatures)


print(f"The average temperature for the week is {average_temperature} degrees.")
