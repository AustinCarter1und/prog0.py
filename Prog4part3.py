# name: Austin Carter
# email: austin.carter.1@und.edu

value = int(input("Enter value: "))

i = 2
while i <= value:
    if value % i == 0:
        print("Largest factor:", i)
        break
    i += 1
