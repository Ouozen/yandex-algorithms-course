from unittest.mock import patch
from tqdm import tqdm


def my_function():
    G1_1, G2_1 = list(map(int, input().split(':')))
    G1_2, G2_2 = list(map(int, input().split(':')))
    type = int(input())

    k = G2_1 + G2_2
    l = k - G1_1 - G1_2

    if G1_1 + G1_2 > G2_1 + G2_2:
        return 0
    elif (type == 2 and G1_1 > G2_2) or (type == 1 and G1_2 + l > G2_1):
        return l
    else:
        return l + 1


def test_my_function(f1, f2, f3, answer):
    with patch('builtins.input', side_effect=[f1, f2, f3]):
        test_answer = my_function()
        # print(test_answer)
        assert test_answer == answer


if __name__ == "__main__":
    test_case = [
        ['0:0', '0:0', '1', 1],
        ['0:2', '0:3', '1', 5],
        ['0:2', '0:3', '2', 6],
        ['0:3', '2:0', '1', 2],
        ['0:0', '0:0', '2', 1],
        ['5:5', '0:0', '1', 1],
        ['5:5', '0:0', '2', 0],
        ['5:5', '4:4', '1', 1],
        ['5:5', '4:4', '2', 0],
        ['0:0', '0:5', '1', 5],
        ['5:4', '4:5', '1', 1],
        ['5:4', '3:4', '2', 0],
        ['2:3', '3:2', '1', 1],
        ['2:3', '3:2', '2', 1],
        ['5:5', '5:5', '1', 1],
        ['5:5', '5:5', '2', 1],
        ['5:5', '0:5', '1', 6],
        ['5:5', '0:4', '2', 4],
        ['0:5', '0:5', '1', 10],
        ['0:5', '0:5', '2', 11],
        ['1:4', '1:3', '1', 5],
        ['1:4', '1:3', '2', 6],
        ['2:0', '3:0', '1', 0],
        ['2:0', '3:0', '2', 0],
    ]
    for f1, f2, f3, answer in tqdm(test_case):
        test_my_function(f1, f2, f3, answer)