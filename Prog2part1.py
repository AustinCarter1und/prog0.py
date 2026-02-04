# Name: Austin Carter
# Email: austin.carter.1@und.edu

checks = int(input("Number of checks: "))

base_fee = 10.00

if checks < 20:
    rate = 0.12
elif checks <= 39:
    rate = 0.10
elif checks <= 59:
    rate = 0.08
else:
    rate = 0.06

service_fee = base_fee + (checks * rate)

print(f"${service_fee:.2f}")

