# name: Austin Carter
# email: austin.carter.1@und.edu

value = int(input("Enter value: "))

i = value - 1
while i > 0:
    if value % i == 0:
        print("Largest factor:", i)
        break
    i -= 1
