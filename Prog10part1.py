# Author: Austin Carter
# Email: austin.carter.1@und.edu

def main():
    students = {}

    # Collect student data
    while True:
        name = input("Enter student name (blank to stop): ").strip()
        if name == "":
            break

        # Ask for credits (integer)
        credits_str = input("Enter completed credits: ").strip()

        # Convert to int (assignment guarantees integer input)
        credits = int(credits_str)

        # Store in dictionary
        students[name] = credits

    # Ask for output filename
    filename = input("Enter output filename: ").strip()

    # Write dictionary to file
    with open(filename, "
