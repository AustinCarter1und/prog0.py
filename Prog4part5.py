# name: Austin Carter
# email: austin.carter.1@und.edu

width = int(input("Enter width: "))
height = int(input("Enter height: "))
char = input("Enter character: ")

for h in range(height):
    line = ""
    for w in range(width):
        line += char
    print(line)
