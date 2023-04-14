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
        return -1
if trees_item[0] != 0:
    tree = [trees_item[0], [], []]
    print("1", end=" ")

    for i in range(len(trees_item)):
        if trees_item[i] != 0:
            lev = add(tree, trees_item[i], 1)
            if lev > 0:
                print(lev, end=" ")

#print(tree)