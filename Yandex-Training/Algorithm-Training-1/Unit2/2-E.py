#n = int(input())
arr = list(map(int, input().split()))

# ищем максимум
max = max(arr)
winner = set()
vas_num = -1
vas_ball = -1
for i in range(0, len(arr)):
    #print(i)
    if arr[i] == max:
        winner.add(i)
    # ищем васю
    if i >0 and i < len(arr) - 1: # вася не первы и не последний
        #print("check {}".format(i))
        if arr[i] % 5 == 0 and arr[i] % 10 != 0:
            if len(winner) > 0 and min(winner) < i:
                if arr[i+1] < arr[i]:
                    if vas_ball < arr[i]:
                        vas_num = i
                        vas_ball = arr[i]
order_arr = sorted(arr, reverse=True)
mesto=1
j=1
for i in order_arr:
    if i == vas_ball:
        mesto = j
        break
    j+=1
if vas_num == -1:
    mesto = 0
#print(order_arr)
print("Вася метнул на {}. КАКИМ МЕТАЛ - {}. Место васи- {}".format(vas_ball, vas_num+1, mesto))
#print(mesto)
