# Name: Austin Carter
# Email: austin.carter.1@und.edu

credits = int(input("Number of completed credits: "))

if credits <= 23:
    rank = "Freshman"
elif credits <= 59:
    rank = "Sophomore"
elif credits <= 89:
    rank = "Junior"
else:
    rank = "Senior"

print(rank)
