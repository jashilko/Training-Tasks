w, h, n = list(map(int, input().split()))

def square(in_x):
    ost = n % in_x # Остаток
    if ost > 0:
        if in_x * w < (n // in_x) * h:
            # Добавляем ширины
            total_w = w * (in_x + ost)
            total_h = h * (n // in_x)
        else:
            # добавляем высоты
            total_w = w * (in_x)
            total_h = h * (n // in_x + ost)
    else:
        total_w = w * (in_x)
        total_h = h * (n // in_x)

    sqr = max(total_h, total_w) ** 2
    return sqr

def check(in_x):
    if in_x < n:
        return square(in_x + 1) >= square(in_x) # функция возрастает
    else:
        return True

def lbinsearch():
    l = 1
    r = n
    while l +1 < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m - 1
    return l

print((lbinsearch()))