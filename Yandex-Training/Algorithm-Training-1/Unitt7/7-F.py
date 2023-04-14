import datetime

n = int(input()) # людей
events = []
for i in range(n):
    ds, ms, ys, de, me, ye = list(map(int, input().split()))
    date_start = datetime.date(ys, ms, ds)
    if ms == 2 and ds == 29:
        date_18 = datetime.date(ys + 18, 3, 1)
    else:
        date_18 = datetime.date(ys+18, ms, ds)
    date_80 = datetime.date(ys+80, ms, ds)
    date_end = datetime.date(ye, me, de)
    if date_18 < date_end:
        events.append((date_18, 1, i+1))
        if date_80 < date_end:
            events.append((date_80, -1, i+1))
        else:
            events.append((date_end, -1, i+1))
events.sort()
#print(events)
#list_of_set = [] #список множеств
people_set = set()
is_add = True
for i in range(len(events)):
    if events[i][1] == 1: # появился в 18
        people_set.add(events[i][2])
        is_add = True
    if events[i][1] == -1: # уходит из множества
        if is_add:
            #list_of_set.append(people_set)
            is_add = False
            print(*people_set)
        people_set = people_set.copy()
        people_set.remove(events[i][2])

if is_add:
    print(0)


#print(*list_of_set)


#print(events)
