# Austin Carter
# austin.carter.1@und.edu

def fillList(fileName):
    try:
        infile = open(fileName, "r")
    except:
        return None

    values = []
    for line in infile:
        line = line.strip()
        if line != "":
            values.append(float(line))
    infile.close()
    return values


def createList(size, defaultValue):
    newList = []
    for _ in range(size):
        newList.append(defaultValue)
    return newList


def adjustList(theList, delta, maxValue):
    for i in range(len(theList)):
        newVal = theList[i] + delta
        if newVal > maxValue:
            theList[i] = maxValue
        else:
            theList[i] = newVal


def startsWith(strList, strToFind):
    result = []
    target = strToFind.lower()

    for s in strList:
        if len(s) > 0 and s[0].lower() == target:
            result.append(s)

    return result


def findFirst(theList, valueToFind):
    for i in range(len(theList)):
        if theList[i] == valueToFind:
            return i
    return -1


def findLast(theList, valueToFind):
    lastIndex = -1
    for i in range(len(theList)):
        if theList[i] == valueToFind:
            lastIndex = i
    return lastIndex


def findMax(theList):
    largest = theList[0]
    for v in theList:
        if v > largest:
            largest = v
    return largest


def findMin(theList):
    smallest = theList[0]
    for v in theList):
        if v < smallest:
            smallest = v
    return smallest


def calcRange(theList):
    return findMax(theList) - findMin(theList)


def main():
    # Test 1: fillList
    fileName = input("Enter a filename: ")
    values = fillList(fileName)

    if values is None:
        print("File not found.")
    else:
        print("Values:", values)
        print("Min:", findMin(values))
        print("Max:", findMax(values))
        print("Range:", calcRange(values))

        adjustList(values, 2, 100)
        print("Adjusted values:", values)

    # Test 2: createList
    testList = createList(5, 10)
    print("\nCreated list:", testList)

    # Test findFirst and findLast
    print("First 10:", findFirst(testList, 10))
    print("Last 10:", findLast(testList, 10))

    # Test startsWith
    names = ["Sam", "sarah", "Bob", "steve", "Alice"]
    print("\nNames starting with 's':", startsWith(names, "s"))


main()
