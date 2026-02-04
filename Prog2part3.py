# Prog2part3.py
# Author: Austin Carter
# Email: austin.carter.1@und.edu

# Ask for numbers and operator
num1 = float(input("Enter the first number: "))
op = input("Enter the operation: ")
num2 = float(input("Enter the second number: "))

# Perform the operation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "//":
    result = num1 // num2
else:
    result = "Invalid operator"

# Display result
print("The result is:", result)



