from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    top = 0
    point = 0
    N = int(input())
    berries = list()
    for step in range(1, N + 1):
        inp = list(map(int, input().split()))
        diff_inp = inp[0] - inp[1]
        berries.append([*inp, diff_inp, step])

    sorted_berries = sorted(berries, reverse=True, key=lambda berry: berry[2])
    for index, berry in enumerate(sorted_berries):
        if berry[2] < 0:
            sorted_berries = sorted_berries[:index] + sorted(sorted_berries[index:], reverse=True, key=lambda berry: berry[0])
            break

    for berry in sorted_berries:
        point += berry[0]
        if point > top:
            top = point
        point -= berry[1]

    return str(top) + ' ' + ' '.join([str(step[-1]) for step in sorted_berries])

def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['3', '1 5', '8 2', '4 4', '10 2 3 1'],
        ['2', '7 6', '7 4', '10 2 1'],
        ['2', '9 8', '7 2', '14 2 1'],
        ['7', '160714711 449656269', '822889311 446755913', '135599877 389312924', '448565595 480845266', '561330066 605997004', '61020590 573085537', '715477619 181424399', '1471516684 2 7 5 1 3 4 6'],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)