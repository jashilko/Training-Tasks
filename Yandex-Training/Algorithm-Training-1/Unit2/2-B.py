pred = -2000000000
type = ""
while 1 == 1:
    a = int(input())
    if a == -2000000000:
        break
    else:
        if pred != -2000000000:
            if a > pred:
                if type == "CONSTANT":
                    type = "WEAKLY ASCENDING"
                elif type in ["DESCENDING", "WEAKLY DESCENDING"]:
                    type = "RANDOM"
                elif type == "":
                    type = "ASCENDING"
            if a == pred:
                if type == "ASCENDING":
                    type = "WEAKLY ASCENDING"
                elif type == "DESCENDING":
                    type = "WEAKLY DESCENDING"
                elif type == "":
                    type = "CONSTANT"
            if a < pred:
                if type == "CONSTANT":
                    type = "WEAKLY DESCENDING"
                elif type in ["ASCENDING", "WEAKLY ASCENDING"]:
                    type = "RANDOM"
                elif type == "":
                    type = "DESCENDING"
        pred = a
if type == "":
    type = "CONSTANT"
print(type)