# Prog12.py
# Austin Carter
# University of North Dakota

def average(dictionary):
    if len(dictionary) == 0:
        return -1
    total = 0
    count = 0
    for name in dictionary:
        total += dictionary[name]
        count += 1
    return total / count


def averageIf(dictionary, lowLimit):
    total = 0
    count = 0
    for name in dictionary:
        if dictionary[name] >= lowLimit:
            total += dictionary[name]
            count += 1
    if count == 0:
        return -1
    return total / count


def removeStudent(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        return True
    return False


def countWithinRange(dictionary, lowLimit, highLimit):
    count = 0
    for name in dictionary:
        score = dictionary[name]
        if lowLimit <= score <= highLimit:
            count += 1
    return count


def subset(dictionary, lowLimit, highLimit):
    newDict = {}
    for name in dictionary:
        score = dictionary[name]
        if lowLimit <= score <= highLimit:
            newDict[name] = score
    return newDict


def students(dictionary):
    # Must return names in ascending order WITHOUT using sorted()
    names = list(dictionary.keys())

    # Manual alphabetical sort (bubble sort)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[j] < names[i]:
                temp = names[i]
                names[i] = names[j]
                names[j] = temp

    return names


def allMetThreshold(dictionary, threshold):
    for name in dictionary:
        if dictionary[name] < threshold:
            return False
    return True


def updateScore(dictionary, change, upperLimit):
    for name in dictionary:
        newScore = dictionary[name] + change
        if newScore > upperLimit:
            newScore = upperLimit
        dictionary[name] = newScore


def main():
    # Create multiple quiz dictionaries
    quiz1 = {"Alice": 45, "Ben": 38, "Cara": 50, "Dylan": 42}
    quiz2 = {"Alice": 18, "Ben": 25, "Cara": 30, "Evan": 12}

    # Test average
    print("Average quiz1:", average(quiz1))
    print("Average quiz2:", average(quiz2))

    # Test averageIf
    print("Average quiz1 (>=40):", averageIf(quiz1, 40))

    # Test removeStudent
    print("Remove Ben from quiz1:", removeStudent(quiz1, "Ben"))
    print("Remove Zoe from quiz1:", removeStudent(quiz1, "Zoe"))

    # Test countWithinRange
    print("Count quiz2 scores 15–30:", countWithinRange(quiz2, 15, 30))

    # Test subset
    print("Subset quiz1 scores 40–50:", subset(quiz1, 40, 50))

    # Test students
    print("Students in quiz2:", students(quiz2))

    # Test allMetThreshold
    print("All quiz1 >= 40:", allMetThreshold(quiz1, 40))

    # Test updateScore
    updateScore(quiz2, 5, 30)
    print("Quiz2 after +5 (max 30):", quiz2)


if __name__ == "__main__":
    main()
