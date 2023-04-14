with open("input.txt", "r") as file:
    n, k = list(map(int, file.readline().split()))
    cars_num = list(map(int, file.readline().split()))

cnt = 0
pref_sum = []
pref_sum.append(0)
sum = 0
for i in range(n):
    sum += cars_num[i]
    pref_sum.append(sum)

#print(pref_sum)

left = 0
right = 0
for left in range(len(pref_sum)):
    while right < len(pref_sum) and pref_sum[right] - pref_sum[left] != k:
        right += 1
    if right < len(pref_sum) and left  < len(pref_sum) and pref_sum[right] - pref_sum[left] == k:
        cnt += 1



print(cnt)
    