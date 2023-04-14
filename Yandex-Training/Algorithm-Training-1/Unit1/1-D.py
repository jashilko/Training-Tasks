a = int(input())
b = int(input())
c = int(input())

x = (c**2 - b) / a
if c<0 or int(x) != float(x):
    print("NO SOLUTION")
elif c**2 == -b:
    print("MANY SOLUTION")
else:
    print(int(x))

