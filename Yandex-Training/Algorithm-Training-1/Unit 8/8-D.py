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

def obhod(tree): # обход и печать
    if tree[1]:
        obhod(tree[1])
    print(tree[0])
    if tree[2]:
        obhod(tree[2])

if trees_item[0] != 0:
    tree = [trees_item[0], [], []]

    for i in range(len(trees_item)):
        if trees_item[i] != 0:
            add(tree, trees_item[i])

#print(tree)
obhod(tree)