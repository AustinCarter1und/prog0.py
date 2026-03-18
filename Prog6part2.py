'''
name: Austin Carter
email: austin.carter.1@und.edu
Program 6 Part 2
This program reads values from a file, filters them by a user-specified range,
and reports statistics about the values within that range.
'''

def main():
    filename = input("Enter file name: ")

    try:
        infile = open(filename, "r")
    except:
        print("File does not exist")
        return

    data = infile.readlines()
    infile.close()

    if len(data) == 0:
        print("No data in file")
        return

    low = float(input("Enter low limit: "))
    high = float(input("Enter high limit: "))

    count = 0
    total = 0.0
    minimum = None
    maximum = None
    found_low = False
    found_high = False

    for line in data:
        value = float(line.strip())

        if value >= low and value <= high:
            count += 1
            total += value

            if minimum is None or value < minimum:
                minimum = value
            if maximum is None or value > maximum:
                maximum = value

            if value == low:
                found_low = True
            if value == high:
                found_high = True

    if count == 0:
        print("Total number of values within range: 0")
        print("Minimum value: 0")
        print("Maximum value: 0")
        print("Average: 0.00")
        return

    print("Total number of values within range:", count)
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)

    if found_high:
        print("Found value of high limit")
    if found_low:
        print("Found value of low limit")

    average = total / count
    print(f"Average: {average:.2f}")

main()

