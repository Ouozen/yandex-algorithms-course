from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    n, k, d = map(int, input().split())
    nowmod = n % k
    ans = [n]
    flag = True
    for i in range(d):
        for newdigit in range(10):
            newmod = (nowmod * 10 + newdigit) % k
            if newmod == 0:
                ans.append(newdigit)
                nowmod = newmod
                break
        else:
            flag = False
    if flag:
        return int(''.join(map(str, ans)))
    else:
        return -1


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['21 108 1', 216],
        ['5 12 4', -1],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)