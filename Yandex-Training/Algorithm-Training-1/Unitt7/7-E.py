import datetime

n = int(input()) # кол-во касс
duration = 0
max_kass = n
kass = []
for i in range(n):
    ts1, te1, ts2, te2 = list(map(int, input().split()))
    t1 = datetime.timedelta(hours=ts1, minutes=te1)
    t2 = datetime.timedelta(hours=ts2, minutes=te2)
    if t1 == t2:
        max_kass -= 1
        if max_kass == 0:
            duration = 24 * 60 * 60
    elif t1 > t2:
        kass.append((datetime.timedelta(hours=0, minutes=0), -1))
        kass.append((t2, 1))
        kass.append((t1, -1))
        kass.append((datetime.timedelta(hours=24, minutes=00), 1))
    else:
        kass.append((t1, -1))
        kass.append((t2, 1))

kass.sort()
#print(*kass)
counter = 0

date_start = datetime.timedelta(hours=0, minutes=0)
for i in range(len(kass)):
    if kass[i][1] == -1:
        counter += 1
        if counter == max_kass:
            date_start = kass[i][0]
    else:
        counter -= 1
        if counter == max_kass - 1:
            tdiff = kass[i][0] - date_start
            duration += tdiff.total_seconds()
            date_start = datetime.timedelta(hours=0, minutes=0)
print(int(duration/60))


