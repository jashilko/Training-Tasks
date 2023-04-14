trees_item = list(map(int, input().split()))



def add(root, x, level):
    if x < root[0]: # идём влево
        level += 1
        if not root[1]:
            root[1] = [x, [], []]

        else:
            level = add(root[1], x, level)
        return level
    elif x > root[0]: # идём вправо
        level += 1
        if not root[2]:
            root[2] = [x, [], []]
        else:
            level = add(root[2], x, level)
        return level
    else: # равны
        return 0

tree = [trees_item[0], [], []]
max_lens = 0

for i in range(len(trees_item)):
    if trees_item[i] != 0:
        lev = add(tree, trees_item[i], 1)
        max_lens = max(lev, max_lens)
        #print("Добавили {}, уровень {}".format(trees_item[i], lev))
    else:
        print(max_lens)
#print(tree)