from unittest.mock import patch
from tqdm import tqdm


def algorithm():
    pass


def test_algorithm(f1, f2, answer):
    with patch('builtins.input', side_effect=[f1, f2]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == answer


if __name__ == "__main__":
    test_case = [
        # test case here in the lists
    ]
    for f1, f2, answer in tqdm(test_case):
        test_algorithm(f1, f2, answer)