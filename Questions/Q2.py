def bitwise_calculator(a, b, operation):
    if operation == "AND":
        return a & b
    elif operation == "OR":
        return a | b
    elif operation == "XOR":
        return a ^ b
    elif operation == "NOT A":
        return ~a
    elif operation == "NOT B":
        return ~b
    elif operation == "LEFT SHIFT A":
        return a << b
    elif operation == "RIGHT SHIFT A":
        return a >> b
    else:
        return "Invalid operation"

print("Bitwise Operator Calculator")
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
print("Available operations: AND, OR, XOR, NOT A, NOT B, LEFT SHIFT A, RIGHT SHIFT A")
operation = input("Enter the bitwise operation to perform: ").strip().upper()

result = bitwise_calculator(a, b, operation)
print(f"The result of {operation} operation is: {result}")

