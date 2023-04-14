n, k = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1)

def lbinsearch(one_k):
    l = 0
    r = n-1
    while l < r:
        m = (l + r) // 2
        if arr1[m] >= one_k:
            r = m
        else:
            l = m +1
    return "YES" if arr1[l] == one_k else "NO"

for i in range(k):
    print(lbinsearch(arr2[i]))