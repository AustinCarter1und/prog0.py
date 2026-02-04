# Name: Austin Carter
# Email: austin.carter.1@und.edu

x = int(input("x: "))
y = int(input("y: "))

if x > 0 and y > 0:
    quadrant = "I"
elif x < 0 and y > 0:
    quadrant = "II"
elif x < 0 and y < 0:
    quadrant = "III"
else:
    quadrant = "IV"

print(f"quadrant {quadrant}")
