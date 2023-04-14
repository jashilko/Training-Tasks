trees_item = list(map(int, input().split()))



def add(root, x): #Добавление узла
    if x < root[0]: # идём влево
        if not root[1]:
            root[1] = [x, [], []]
        else:
            add(root[1], x)
    elif x > root[0]: # идём вправо
        if not root[2]:
            root[2] = [x, [], []]
        else:
            add(root[2], x)
    else: # равны
        return -1

def pre_max(tree, pred): # вывести недомаксимальный элемент
    if tree[2]:
        pre_max(tree[2], tree[0])
    else:
        max = tree[0]
        if tree[1]:
            pre_max(tree[1], tree[0])
        if not tree[1] and not tree[2]:
            print(pred)


if trees_item[0] != 0:
    tree = [trees_item[0], [], []]

    for i in range(len(trees_item)):
        if trees_item[i] != 0:
            add(tree, trees_item[i])

#print(tree)
pre_max(tree, -1)