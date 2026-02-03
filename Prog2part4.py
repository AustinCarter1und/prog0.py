name: Austin Carter
email:austin.carter.1@#und.edu
credits = int(input("Number of completed credits: "))

# Determine class rank
if credits <= 23:
    rank = "Freshman"
elif credits <= 59:
    rank = "Sophomore"
elif credits <= 89:
    rank = "Junior"
else:
    rank = "Senior"

# Output result
print("Class rank:", rank)
