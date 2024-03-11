from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    K = int(input())
    x_max, y_max = map(int, input().split())
    x_min = x_max#.copy()
    y_min = y_max#.copy()
    for _ in range(K - 1):
        x, y = map(int, input().split())
        if x > x_max:
            x_max = x
        elif x < x_min:
            x_min = y

        if y > y_max:
            y_max = y
        elif y < y_min:
            y_min = y
    return ' '.join([str(x_min), str(y_min), str(x_max), str(y_max)])


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['4', '1 3', '3 1', '3 5', '6 3', '1 1 6 5'],
        ['1', '1 50', '1 50 1 50'],
        ['3', '1 50', '1 50', '1 50', '1 50 1 50'],
        ['3', '1 2', '1 3', '1 4', '1 2 1 4'],
        ['3', '2 1', '3 1', '4 1', '2 1 4 1'],
        ['3', '-100 -200', '-50 -30', '-60 -150', '-100 -200 -50 -30'],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)