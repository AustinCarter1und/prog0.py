# Ask for inputs
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

# Display result
print("The result is:", result)


