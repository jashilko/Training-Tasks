n, k = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def lbinsearch(one_k):
    l = 0
    r = n-1
    while l < r:
        m = (l + r) // 2
        if arr1[m] >= one_k:
            r = m
        else:
            l = m +1
    #print(r, l)
    if l > 0:
        if abs(arr1[l]-one_k) < abs(arr1[l-1]-one_k):
            return arr1[l]
        else:
            return arr1[l-1]
    else:
        return arr1[l]

for i in range(k):
    print(lbinsearch(arr2[i]))