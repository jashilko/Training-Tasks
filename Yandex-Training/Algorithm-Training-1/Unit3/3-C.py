n, m = list(map(int, input().split()))
ann = set()
bor = set()
for _ in range(n):
    ann.add(int(input()))
for _ in range(m):
    bor.add(int(input()))

#print(ann)
#print(bor)
print(len(ann.intersection(bor)))
print(*sorted(ann.intersection(bor)))
print(len(ann-bor))
print(*sorted(ann-bor))
print(len(bor-ann))
print(*sorted(bor-ann))
