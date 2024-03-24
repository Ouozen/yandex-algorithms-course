from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    N = input()
    num_list = list(map(int, input().split()))

    min_num = min(num_list)
    max_num = max(num_list)
    min_counter = 0
    max_counter = 0

    for num in num_list:
        if abs(min_num - num) > 1:
            min_counter += 1
        if abs(max_num - num) > 1:
            max_counter += 1

    return min(min_counter, max_counter)


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['5', '1 2 3 4 5', 3],
        ['10', '1 1 2 3 5 5 2 2 1 5', 4],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)