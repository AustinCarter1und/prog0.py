# Prog2part1.py
name: Austin Carter
email:austin.carter.1@#und.edu

# Ask for number of checks
checks = int(input("Number of checks: "))

# Base monthly fee
base_fee = 10.00

# Determine check fee rate
if checks < 20:
    rate = 0.12
elif checks <= 39:
    rate = 0.10
elif checks <= 59:
    rate = 0.08
else:
    rate = 0.06

# Calculate total service fee
service_fee = base_fee + (checks * rate)

# Display result rounded to two decimals
print(f"Service fee: ${service_fee:.2f}")
name: Austin Carter
email:austin.carter.1@#und.edu


