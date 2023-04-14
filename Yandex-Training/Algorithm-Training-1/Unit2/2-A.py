inlist = list(map(int, input().split()))

pred=inlist[0]
answer="YES"
for i in range(1, len(inlist)):
    if inlist[i]<=pred:
        answer="NO"
        break
    pred = inlist[i]
print(answer)