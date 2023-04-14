person = {}
def create_acc(name):
    if not name in person:
        person[name] = 0

def add_amount(name, amount):
    create_acc(name)
    person[name] += amount

def withdraw_amount(name, amount):
    create_acc(name)
    person[name] -= amount


def add_percent(percent):
    for key, value in person.items():
        if value > 0:
            person[key] *= (1+percent/100)
            person[key] = int(person[key])

with open("input.txt", "r") as file:
    for line in file:
        dict1 = line.split()
        if dict1[0] == "DEPOSIT":
            add_amount(dict1[1], int(dict1[2]))
        if dict1[0] == "BALANCE":
            if dict1[1] in person:
                print(person[dict1[1]])
            else:
                print("ERROR")
        if dict1[0] == "WITHDRAW":
            withdraw_amount(dict1[1], int(dict1[2]))
        if dict1[0] == "TRANSFER":
            withdraw_amount(dict1[1], int(dict1[3]))
            add_amount(dict1[2], int(dict1[3]))
        if dict1[0] == "INCOME":
            add_percent(int(dict1[1]))

# print(person)