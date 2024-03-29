from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    pass


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        # test case here in the lists
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)