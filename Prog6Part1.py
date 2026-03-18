'''
name: Austin Carter
email: austin.carter.1@und.edu
Program 6 Part 1
This program asks for a filename and writes floating point values (0–100) to it
until the user enters a value outside that range.
'''

def main():
    filename = input("Enter file name: ")

    # Open file for writing
    outfile = open(filename, "w")

    while True:
        value = float(input("Enter a value: "))
        if value < 0 or value > 100:
            break
        outfile.write(str(value) + "\n")

    outfile.close()

main()
