# name: Austin Carter
# email: austin.carter.1@und.edu

num_students = int(input("How many students in the class: "))

fresh = 0
soph = 0
jun = 0
sen = 0

i = 0
while i < num_students:
    rank = input("Enter the student rank: ")
    if rank == "Freshman":
        fresh += 1
    elif rank == "Sophomore":
        soph += 1
    elif rank == "Junior":
        jun += 1
    elif rank == "Senior":
        sen += 1
    i += 1

print("Freshman:", fresh)
print("Sophomores:", soph)
print("Juniors:", jun)
print("Seniors:", sen)
