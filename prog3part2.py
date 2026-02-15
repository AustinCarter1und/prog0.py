# name: Austin Carter
# email: austin.carter.1@und.edu

start_val = int(input("Enter starting value: "))

i = start_val
output = ""

while i >= 0:
    output += str(i) + " "
    i -= 1

print(output)
