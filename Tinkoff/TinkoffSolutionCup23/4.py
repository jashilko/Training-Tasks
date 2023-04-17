from itertools import combinations, product, combinations_with_replacement, permutations


# python 3.10


def find_combinations(text: str) -> list[str]:
    letset = set()
    for i in text:
        letset.add(i)
    text_new = ''.join(letset)
    ans_list = []
    for i in range(len(text)):
        newset = set(permutations(text_new, i + 1))
        for one in newset:
            ans_list.append(''.join(one))
    ans = ""
    ans_list.sort()
    for one in ans_list:
        ans += one + ', '
    print(ans[:-2])



if __name__ == "__main__":
    input_str = input()
    # Необходимо преобразовать список в строку перед выводом.
    find_combinations(input_str)
#
# print(set(permutations('abca', 1)))
# print(set(permutations('abca', 2)))
# print(set(permutations('abca', 3)))

