letters = {}
with open("input1.txt", "r") as file:
    for line in file:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        for one in line:
            if one in letters:
                letters[one] += 1
            else:
                letters[one] = 1

max_val =max(letters.values())
print(max_val)
print(letters)
str_num = 1
while str_num <= max_val + 1:
    str = ""
    for num in letters.values():
