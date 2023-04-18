n = int(input())

v_kisl = list(map(int, input().split()))

def value_kisl(v_kisl):
    # Суть - определить, что последовательность неубывающая
    v_min = v_kisl[0]
    v_max = v_kisl[len(v_kisl) - 1]
    for i in range(len(v_kisl)-1):
        if v_kisl[i] > v_kisl[i+1]:
            return -1
    return (v_max - v_min)

print(value_kisl(v_kisl))