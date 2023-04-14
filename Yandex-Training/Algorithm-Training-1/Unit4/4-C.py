person = {}
with open("input.txt", "r") as file:
    for line in file:
        dict1 = line.split()
        for one in dict1:
            if one in person:
                person[one] = person[one] + 1
            else:
                person[one] = 1
person = dict(sorted(person.items(), key=lambda item: (-item[1], item[0]), reverse=False))
for key in person:
    print(key)
    break