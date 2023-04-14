n, m = list(map(int, input().split()))

events = []

for _ in range(n):
    start, stop = list(map(int, input().split()))
    events.append((min(start, stop), -1, -1))
    events.append((max(start, stop), 1, -1))

dots = list(map(int, input().split()))
#print(dots)
online = 0
for i in range(len(dots)):
    events.append((dots[i], 0, i))
events.sort()
for i in range(len(events)):
    if events[i][1] == -1:
        online += 1
    elif events[i][1] == 1:
        online -= 1
    else:
        dots[events[i][2]] = online
print(*dots)


#print(events)
