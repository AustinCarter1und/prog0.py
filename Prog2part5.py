# Ask for an integer value
value = int(input("Enter an integer value: "))

# Check if the value is within the 400s
if value >= 400 and value <= 499:
    answer = "yes"
else:
    answer = "no"

# Output result
print("Within range?", answer)
