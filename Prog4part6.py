# name: Austin Carter
# email: austin.carter.1@und.edu

pos_total = 0
pos_count = 0
neg_total = 0
neg_count = 0

value = int(input("Enter a value: "))

while value != 0:
    if value > 0:
        pos_total += value
        pos_count += 1
    elif value < 0:
        neg_total += value
        neg_count += 1

    value = int(input("Enter a value: "))

if pos_count > 0:
    print("Average of positive values: {:.2f}".format(pos_total / pos_count))
else:
    print("Average of positive values: N/A")

if neg_count > 0:
    print("Average of negative values: {:.2f}".format(neg_total / neg_count))
else:
    print("Average of negative values: N/A")
