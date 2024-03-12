from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    K = int(input())
    x_max, y_max = map(int, input().split())
    x_min = x_max
    y_min = y_max
    for _ in range(K - 1):
        x, y = map(int, input().split())
        if x > x_max:
            x_max = x
        elif x < x_min:
            x_min = x

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
        ['5', '668 1676', '1810 6372', '3301 4297', '2297 6251', '2598 3714', '668 1676 3301 6372'],
        ['20', '8709 1322', '3438 2462', '8290 5861', '2858 906', '5862 3588', '6394 984', '7634 6392', '5231 4793', '2493 8185', '3832 6656', '9549 9510', '7338 1967', '1747 2457', '570 4095', '9759 7018', '4116 6689', '2880 2429', '5463 1225', '6144 9628', '5656 2142', '570 906 9759 9628'],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)