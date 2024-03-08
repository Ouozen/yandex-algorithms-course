from unittest.mock import patch
from tqdm import tqdm


def algorithm():
    n = int(input())
    click = 0
    for _ in range(n):
        row_space = int(input())
        if row_space == 0:
            continue
        else:
            cel_del = row_space // 4
            ost_del = row_space % 4
            if ost_del == 0:
                click += cel_del
            elif ost_del == 1:
                click += cel_del + 1
            else:
                click += cel_del + 2

    return click


def test_algorithm(f1, f2, f3, f4, f5, f6, answer):
    with patch('builtins.input', side_effect=[f1, f2, f3, f4, f5, f6]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == answer


if __name__ == "__main__":
    test_case = [
        ['5', '1', '4', '12', '9', '0', 8]
    ]
    for f1, f2, f3, f4, f5, f6, answer in tqdm(test_case):
        test_algorithm(f1, f2, f3, f4, f5, f6, answer)