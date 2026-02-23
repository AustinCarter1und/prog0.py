'''
name: Austin Carter
email: austin.carter.1@und.edu
This program defines several functions and tests them in main.
'''

# ------------------------------------------------------------
# Function: square
# Parameters:
#   intValue - an integer whose square will be computed
# Returns:
#   The square of intValue
# Description:
#   This function returns intValue multiplied by itself.
# ------------------------------------------------------------
def square(intValue):
    return intValue * intValue


# ------------------------------------------------------------
# Function: sumOfSquares
# Parameters:
#   intValue - an integer representing the upper bound
# Returns:
#   The sum of the squares from 1 to intValue
#   Returns -1 if intValue is less than 0
# Description:
#   Uses a loop and the square() function to accumulate the sum
#   of squares. Does NOT use built-in sum() or math operations
#   beyond multiplication.
# ------------------------------------------------------------
def sumOfSquares(intValue):
    if intValue < 0:
        return -1

    total = 0
    for i in range(1, intValue + 1):
        total += square(i)
    return total


# ------------------------------------------------------------
# main
# Description:
#   Tests all required functions with sample values.
# ------------------------------------------------------------
def main():
    print("Testing square function:")
    print("square(5) =", square(5))
    print("square(10) =", square(10))

    print("\nTesting sumOfSquares function:")
    print("sumOfSquares(5) =", sumOfSquares(5))   # expected 55
    print("sumOfSquares(10) =", sumOfSquares(10)) # expected 385
    print("sumOfSquares(-3) =", sumOfSquares(-3)) # expected -1


# Call to main
main()
