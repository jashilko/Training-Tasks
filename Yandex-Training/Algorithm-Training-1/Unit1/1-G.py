n, k, m = list(map(int, input().split()))

cnt = 0

def add_cnt(kg):
    new_zag = (kg // k) *  ( k // m)
    return new_zag, kg - m * new_zag

while n > 0:
    zag, n = add_cnt(n)
    cnt += zag
    if (n < m) or (n < k) or (k<m):
        break
print(cnt)
