person = {}
with open("input.txt", "r") as file:
    for line in file:
        name, item, count = line.split()
        if name in person:
            if item in person[name]:
                person[name][item] += int(count)
            else:
                person[name][item] = int(count)
        else:
            person[name] = {}
            person[name][item] = int(count)
#print(person)
person = dict(sorted(person.items()))

for key in person:
    print("{}:".format(key))
    items = dict(sorted(person[key].items()))
    for kk, val in items.items():
        print(kk + " " + str(val))