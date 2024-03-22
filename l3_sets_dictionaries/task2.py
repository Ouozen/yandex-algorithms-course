from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    first_word = input()
    second_word = input()

    first_d = dict()
    second_d = dict()
    for char in first_word:
        first_d[char] = first_d.get(char, 0) + 1
    for char in second_word:
        second_d[char] = second_d.get(char, 0) + 1

    first_res = sorted(first_d.items(), key=lambda char: char[0])
    second_res = sorted(second_d.items(), key=lambda char: char[0])

    if first_res == second_res:
        return "YES"
    else:
        return "NO"


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['dusty', 'study', 'YES'],
        ['rat', 'bat', 'NO'],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)