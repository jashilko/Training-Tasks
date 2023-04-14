n = int(input())
m = int(input())
t = int(input())


def count_of_one_row(n, m):
    return n * 2 + (m-2)*2

def check(row_count):
    # проверяем, что все хорошо
    count_total = n * m - ((n-row_count*2) * (m-row_count*2))
    return count_total <= t

def rbinsearch():
    if count_of_one_row(n, m) > t:
        return 0
    l = 1
    r = min(n, m) // 2
    while l < r:
        x = (l + r + 1) // 2
        if check(x):
            l = x
        else:
            r = x -1
    return l

print(rbinsearch())