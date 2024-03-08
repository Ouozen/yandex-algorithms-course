from unittest.mock import patch
from tqdm import tqdm


def algorithm() -> int:
    P, V = list(map(int, input().split(' ')))
    Q, M = list(map(int, input().split(' ')))

    # определим конечные точки Маши и Васи
    V1, V2 = P + V, P - V
    M1, M2 = Q + M, Q - M

    # определим пересекаются ли их окрестности
    if max(V1, M1) == M1 and min(V2, M2) == M2:
        return M1 - M2 + 1
    elif max(V1, M1) == V1 and min(V2, M2) == V2:
        return V1 - V2 + 1
    elif Q > P and V1 > M2:
        return M1 - V2 + 1
    elif P > Q and M1 > V2:
        return V1 - M2 + 1
    else:
        mod = 1 if V1 == M2 or M1 == V2 else 2
        return (V1 - V2) + (M1 - M2) + mod


def test_algorithm(f1, f2, answer) -> None:
    with patch('builtins.input', side_effect=[f1, f2]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == answer


if __name__ == "__main__":
    test_case = [
        ['0 2', '10 3', 12],
        ['0 5', '7 3', 16],
        ['7 3', '0 5', 16],
        ['0 7', '12 5', 25],
        ['0 7', '0 7', 15],
        ['0 2', '1 5', 11],
        ['1 5', '0 2', 11]
    ]
    for f1, f2, answer in tqdm(test_case):
        test_algorithm(f1, f2, answer)