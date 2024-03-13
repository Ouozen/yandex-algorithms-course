from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    profit = 0
    N, K = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    for index, price_purchase in enumerate(prices):
        index_last = index + K + 1
        for price_sale in prices[index:index_last]:
            if price_sale - price_purchase > profit:
                profit = price_sale - price_purchase

    return profit


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['1 5', '4', 0],
        ['5 2', '1 2 3 4 5', 2],
        ['5 2', '5 4 3 2 1', 0],
        ['1 1', '1', 0]

    ]
    for case in tqdm(test_case):
        test_algorithm(*case)