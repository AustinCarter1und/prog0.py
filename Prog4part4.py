# name: Austin Carter
# email: austin.carter.1@und.edu

text = input("String to search: ")
char = input("Character to count: ")

count = 0
for c in text:
    if c == char:
        count += 1

print("Number of occurrences:", count)
