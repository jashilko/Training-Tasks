

person = {}
with open("input.txt", "r") as file:
    for line in file:
        dict = line.split()
        for one in dict:
            if one in person:
                print(person[one], end=' ')
                person[one] =person[one] + 1
            else:
                print(0, end=' ')
                person[one] = 1