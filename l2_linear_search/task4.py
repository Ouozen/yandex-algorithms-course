from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    pre_board = [1 for _ in range(10)]
    board = [pre_board.copy() for _ in range(10)]
    patterns = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    perimeter = 0

    N = int(input())
    busy_fields = []
    for _ in range(N):
        busy_fields.append(list(map(int, input().split())))

    for field in busy_fields:
        y_field, x_field = field
        board[y_field][x_field] = 0

    for field in busy_fields:
        y_field, x_field = field
        for pattern in patterns:
            y_pattern, x_pattern = pattern
            y_check, x_check = y_field + 1 * y_pattern, x_field + 1 * x_pattern
            perimeter += board[y_check][x_check]

    return perimeter


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['1', '8 8', 4],
        ['3', '1 1', '1 2', '2 1', 8],
        ['1', '5 6', 4]
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)