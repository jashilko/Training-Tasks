n, m = list(map(int, input().split()))

desks = []

for i in range(m):
    start, stop = list(map(int, input().split()))
    desks.append((start, -1))
    desks.append((stop, 1))
#print(desks)
desks.sort()
prepod_look = 0
start_look = -1
len_look = 0
free_student_count = 0
for i in range(len(desks)):
    if desks[i][1] == -1:
        prepod_look += 1
        if prepod_look == 1:
            start_look = desks[i][0]
    else:
        prepod_look -= 1
        if prepod_look == 0:
            len_look += desks[i][0] - start_look + 1


#print(desks)
print(n - len_look)
