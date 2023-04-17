# python 3.10


def get_answer_mask(text: str) -> list[int]:
    ans, good = list(text.split(', '))
    good_ans = {}
    for i in good:
        if i in good_ans:
            good_ans[i] += 1
        else:
            good_ans[i] = 1
    #print(good_ans)
    # Бежим по ответу пользователя c точным совпадением
    mass_ans = [-1] * 5
    for i in range(len(ans)):
        if ans[i] == good[i]:
            mass_ans[i] = 1
            good_ans[ans[i]] -= 1

    #print(mass_ans)
    #print(good_ans)
    for i in range(len(ans)):
        if mass_ans[i] != 1:
            if ans[i] in good_ans and good_ans[ans[i]] > 0:
                mass_ans[i] = 0
                good_ans[ans[i]] -= 1

    #print(*mass_ans)
    #print(good_ans)\
    ans_str = ""
    for one in mass_ans:
        ans_str += str(one) + ', '
    print(ans_str[:-2])

if __name__ == "__main__":
    input_str = input()
    # Необходимо преобразовать список в строку перед выводом.
    get_answer_mask(input_str)
