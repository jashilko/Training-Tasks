a = int(input())
b = int(input())
c = int(input())

len = a + b + c
#grades = tuple([2] * a) + tuple([3] * b) + tuple([4] * c)
sum = 2 * a + 3 * b + 4 * c
#print(grades, sum)

def check(count_5):
    return 2*(sum + 5 * count_5) >= 7 * (len + count_5)

def lbinsearch():
    l = 0
    r = len
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m +1
    return l

print(lbinsearch())