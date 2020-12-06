CHAR_TO_NUM = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}


def get_number_of_yes(answers):
    answer_list = []
    num_in_group = 0
    for i in range(26):
        answer_list.append(0)
    for char in answers:
        if char != '\n':
            answer_list[CHAR_TO_NUM.get(char)] += 1
        else:
            num_in_group += 1
    result = 0
    for answer in answer_list:
        if answer == num_in_group:
            result += 1
    return result


if __name__ == '__main__':
    results = []
    with open('AoCDay6.txt') as file:
        answers = ''
        for line in file:
            if line != '\n':
                answers += line
            else:
                results.append(get_number_of_yes(answers))
                answers = ''
        results.append(get_number_of_yes(answers))
    print(sum(results))
