
def work(troom, tcond, mode):
    if mode == "freeze" and troom > tcond:
        return tcond
    if mode == "heat" and troom < tcond:
        return tcond
    if mode == "auto":
        return  tcond
    return  troom


troom, tcond = list(map(int, input().split()))
mode = input()
print(work(troom, tcond, mode))
