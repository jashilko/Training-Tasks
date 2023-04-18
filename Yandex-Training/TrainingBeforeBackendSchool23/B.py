n = int(input())

# Заполняем рассадку
seats = []
for i in range(n):
    l, r = list(input().split('_'))
    seats.append([l, r])
#print(seats)

# Проверяем, смогут ли они сесть
def can_you_seat(seats, num, side, pos):
    print(num, side, pos)
    if side == "left":
        side_num = 0
    else:
        side_num = 1
    for i in range(len(seats)):
        #if
        pass
m = int(input())
# Обходим группы пассажиров
for i in range(m):
    num, side, pos = list(input().split())
    can_you_seat(seats, num, side, pos)
