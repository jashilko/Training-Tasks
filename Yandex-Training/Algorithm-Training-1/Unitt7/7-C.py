n, d = list(map(int, input().split()))
stud = list(map(int, input().split()))

stud_list = []
for i in range(n):
    stud_list.append([stud[i], -1, i, -999, 0])
    stud_list.append([stud[i]+d, 1, i, -999, 0])
stud_list.sort()

count_listener = 0
last_ticket = 1
max_ticket = 1
for i in range(len(stud_list)):
    if stud_list[i][1] == -1: # начал слушать вперед
        if count_listener > 0: # кто-то нас прослушивает
            if last_ticket - count_listener > 0:
                cur_ticket = last_ticket - count_listener
            else:
                cur_ticket = max_ticket + 1
                max_ticket = cur_ticket
            last_ticket = cur_ticket
        else:
            cur_ticket = last_ticket
        stud_list[i][3] = cur_ticket
        count_listener += 1

    if stud_list[i][1] == 1:
        count_listener -= 1
    stud_list[i][4] = count_listener

itog = [i[3] for i in sorted(filter(lambda sob: sob[1] == -1, stud_list), key=lambda item: item[2])]
print(len(set(itog)))
print(*itog)
#print(stud_list)
