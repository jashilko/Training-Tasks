a1, b1, a2, b2 = list(map(int, input().split()))
min = (a1 + a2) * (max(b1, b2))
h = (a1 + a2)
w = (max(b1, b2))
v = 1
if (a1 + b2) * (max(a2, b1)) < min:
    min =  (a1 + b2) * (max(a2, b1))
    h = (a1 + b2)
    w = (max(a2, b1))
    v=2

if (b1 + a2) * (max(b2, a1)) < min:
    min =  (b1 + a2) * (max(b2, a1))
    h = (b1 + a2)
    w = (max(b2, a1))
    v=3

if (b1 + b2) * (max(a2, a1)) < min:
    min =  (b1 + b2) * (max(a2, a1))
    h = (b1 + b2)
    w =(max(a2, a1))
    v=4

print(w, h)