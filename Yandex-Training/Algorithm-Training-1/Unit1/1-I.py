a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if ((a<=d)and (b<=e)) or (a<=e and b<=d) or (b<=d and c<=e) or (b<=e and c<=d) or (a<=d and c<=e) or  (a<=e and c<=d):
    print("YES")
else:
    print("NO")
