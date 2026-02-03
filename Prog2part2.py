# Ask for x and y values
x = int(input("x: "))
y = int(input("y: "))

# Determine quadrant
if x > 0 and y > 0:
    quadrant = "I"
elif x < 0 and y > 0:
    quadrant = "II"
elif x < 0 and y < 0:
    quadrant = "III"
else:
    quadrant = "IV"

# Output result
print(f"({x}, {y}) is in: quadrant {quadrant}")
