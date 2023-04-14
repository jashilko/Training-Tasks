arr = list(map(int, input().split()))

maxPlus1 = -1
maxPlus2 = -1
maxMinis1 = 1
maxMinus2 = 1

for n in arr:
    if n >= 0:
        if maxPlus1 == -1:
            maxPlus1 = n
        elif n > maxPlus1:
            maxPlus2 = maxPlus1
            maxPlus1 = n
        elif maxPlus2 == -1:
            maxPlus2 = n
        elif n > maxPlus2:
            maxPlus2 = n
    elif n < 0:
        if maxMinis1 == 1:
            maxMinis1 = n
        elif n < maxMinis1:
            maxMinus2 = maxMinis1
            maxMinis1 = n
        elif maxMinus2 == -1:
            maxMinus2 = n
        elif n < maxMinus2:
            maxMinus2 = n

#print("MaxPlus1: {}, MaxPlus2: {}".format(maxPlus1, maxPlus2))
#print("MaxMinus1: {}, MaxMinus2: {}".format(maxMinis1, maxMinus2))

max = 0
es = 0
if maxPlus1 >= 0 and maxPlus2 >= 0:
    max = maxPlus1 * maxPlus2
    one = maxPlus2
    two = maxPlus1
    es = 1

if maxMinis1 < 0 and maxMinus2 < 0:
    if es == 0 or es == 1 and maxMinis1 * maxMinus2 > max:
        one = maxMinis1
        two = maxMinus2
        es = 1
if maxPlus1 >= 0 and maxMinis1 < 0:
    if es == 0:
        one = maxMinis1
        two = maxPlus1
#print("one - {} two - {}. Res = {}".format(one, two, one * two))
print(one, two)
