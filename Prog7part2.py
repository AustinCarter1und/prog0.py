'''
name: Austin Carter
email: austin.carter.1@und.edu
Program 7 Part 2
This program reads class information from a file, displays it in aligned
columns, and calculates GPA and other statistics.
'''

def main():
    filename = input("Enter file name: ")

    try:
        infile = open(filename, "r")
    except:
        print("File does not exist")
        return

    total_credits = 0
    passed_credits = 0
    class_attempts = 0
    class_passed = 0
    honor_points = 0.0

    for line in infile:
        line = line.strip()
        if line == "":
            continue

        classname, grade, credits = line.split(":")
        grade = grade.upper()
        credits = int(credits)

        print(f"{classname:<8} {grade:<1} {credits:>2}")

        class_attempts += 1
        total_credits += credits

        if grade != "F":
            passed_credits += credits
            class_passed += 1

        if grade == "A":
            honor_points += credits * 4
        elif grade == "B":
            honor_points += credits * 3
        elif grade == "C":
            honor_points += credits * 2
        elif grade == "D":
            honor_points += credits * 1
        elif grade == "F":
            honor_points += credits * 0

    infile.close()

    print()

    if total_credits == 0:
        gpa = 0.0
    else:
        gpa = honor_points / total_credits

    print(f"GPA: {gpa:.3f}")
    print(f"Credits attempts {total_credits:>5}")
    print(f"Credits passed   {passed_credits:>5}")
    print(f"Classes attempted{class_attempts:>5}")
    print(f"Classes passed   {class_passed:>5}")

main()

