'''
name: Austin Carter
email: austin.carter.1@und.edu
Program 7 Part 1
This program asks the user for class information and writes each class,
its grade, and its credits to a file using colon-separated formatting.
'''

def main():
    filename = input("Enter file name: ")
    outfile = open(filename, "w")

    while True:
        classname = input("Enter class name: ")
        if classname == "":
            break

        grade = input("Enter anticipated grade: ").upper()
        credits = input("Enter number of credits: ")

        outfile.write(classname + ":" + grade + ":" + credits + "\n")

    outfile.close()

main()
