n = int(input())
dict = {}
for _ in range(n):
    a, b = input().split()
    dict[a] = b
    dict[b] = a
print(dict[input()])