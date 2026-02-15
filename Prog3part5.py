# name: Austin Carter
# email: austin.carter.1@und.edu

start_val = int(input("Enter starting value: "))
end_val = int(input("Enter ending value: "))

i = start_val

if start_val <= end_val:
    while i <= end_val:
        print(i)
        i += 1
else:
    while i >= end_val:
        print(i)
        i -= 1
