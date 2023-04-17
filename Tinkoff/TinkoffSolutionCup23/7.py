def compress_sequence(text: str) -> list[tuple[int, int]]:
    ans = []
    if text:
        text = list(map(int, text.split(', ')))
    #print(text)
    if text:
        last_word = text[0]
    else:
        return []
    num_word = 0
    for i in text:
        if i == last_word:
            num_word += 1
        else:
            ans.append((last_word, num_word))
            last_word = i
            num_word = 1
    ans.append((last_word, num_word))
    ans_str = ""
    for one in ans:
        ans_str += str(one) + ', '
    print(ans_str[:-2])
    return ans_str


if __name__ == "__main__":
    input_str = input()
    # Необходимо преобразовать список в строку перед выводом.
    a = compress_sequence(input_str)
    #compress_sequence(input_str)
