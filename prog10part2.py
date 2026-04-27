# Prog10part2.py
# Author: Austin Carter
# Email: austin.carter.1@und.edu
# Description:
# Part 2 – Read student/credit data from a file, process the dictionary
# using required functions, and display results.

def readStudentInfo(fileName):
    students = {}
    with open(fileName, "r") as infile:
        for line in infile:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("\t")
            name = parts[0]
            credits = int(parts[1])
            students[name] = credits
    return students


def numStudents(students):
    count = 0
    for _ in students:
        count += 1
    return count


def removeStudent(students, studentName):
    if studentName in students:
        del students[studentName]
        return True
    return False


def updateStudent(students, studentName, credits):
    if studentName in students:
        students[studentName] = students[studentName] + credits
    else:
        students[studentName] = credits


def studentsWithCredits(students, lowLimit, highLimit):
    result = []
    for name in students:
        credits = students[name]
        if credits >= lowLimit and credits <= highLimit:
            result.append(name)
    return result


def freshmenStudents(students):
    # Must use studentsWithCredits ONLY
    return studentsWithCredits(students, 0, 23)


def eligibleForGraduation(students, studentName, gpa):
    if studentName not in students:
        return False
    credits = students[studentName]
    if credits >= 120 and gpa >= 2.2:
        return True
    return False


def printStudents(title, students):
    # Title + column headers = exactly two lines
    print(title)
    print("Name                 Credits")

    # Sort alphabetically WITHOUT using sorted() or sort()
    # Manual alphabetical ordering
    names = []
    for name in students:
        names.append(name)

    # Simple manual selection sort
    for i in range(len(names)):
        min_index = i
        for j in range(i + 1, len(names)):
            if names[j] < names[min_index]:
                min_index = j
        if min_index != i:
            temp = names[i]
            names[i] = names[min_index]
            names[min_index] = temp

    # Print aligned table
    for name in names:
        credits = students[name]
        print(f"{name:<20}{credits:>7}")


def main():
    filename = input("Enter filename: ").strip()
    students = readStudentInfo(filename)

    # Call required functions and display results
    print("Number of students:", numStudents(students))

    # Demonstration calls (autograder may override input)
    # Remove a student
    removed = removeStudent(students, "Tom")
    print("Removed Tom:", removed)

    # Update/add a student
    updateStudent(students, "Alice", 10)

    # Students in credit range
    midLevel = studentsWithCredits(students, 30, 90)
    print("Students with 30–90 credits:", midLevel)

    # Freshmen
    fresh = freshmenStudents(students)
    print("Freshmen:", fresh)

    # Graduation eligibility example
    eligible = eligibleForGraduation(students, "Alice", 3.0)
    print("Alice eligible for graduation:", eligible)

    # Print table
    printStudents("Student Credit Report", students)


if __name__ == "__main__":
    main()
