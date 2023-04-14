with open("input.txt", "r") as file:
    n = int(file.readline())
    list1 = list(map(int, file.readline().split()))
    k = int(file.readline())
    list2 = list(map(int, file.readline().split()))

#print(n, k)
dict = {}

for i in range(n):
    dict[i+1] = list1[i]



for i in range(k):
    dict[list2[i]] -= 1
#print(len(dict))
for i in range(len(dict)):
    if dict[i+1] < 0:
        print("YES", '')
    else:
        print("NO", '')
