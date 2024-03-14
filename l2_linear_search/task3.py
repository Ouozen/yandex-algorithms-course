from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    N = int(input())
    ropes = list(map(int, input().split()))

    max_rope = ropes[0]
    for rope in ropes[1:]:
        if rope > max_rope:
            max_rope = rope

    if 2 * max_rope - sum(ropes) > 0:
        return 2 * max_rope - sum(ropes)
    else:
        return sum(ropes)


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['4', '1 5 2 1', 1],
        ['4', '5 12 4 3', 24],
        ['4', '6 11 4 3', 24],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)