from unittest.mock import patch
from tqdm import tqdm


def algorithm() -> int:
    figures = {"R": [], "B": []}
    cnt = 64
    for row in range(8):
        line = list(input().strip())
        while "R" in line:
            column = line.index("R")
            figures["R"].append([row, column])
            line[column] = "*"
        while "B" in line:
            column = line.index("B")
            figures["B"].append([row, column])
            line[column] = "*"
    if figures == {"R": [], "B": []}:
        return cnt
    for row in range(8):
        for column in range(8):
            subtract = False
            for figure, coord in figures.items():
                for r_fig, c_fig in coord:
                    x_dif = abs(row - r_fig)
                    y_dif = abs(column - c_fig)
                    if figure == "B" and x_dif == y_dif and not subtract:
                        cnt -= 1
                        subtract = True
                    elif figure == "R" and (x_dif == 0 or y_dif == 0) and not subtract:
                        cnt -= 1
                        subtract = True
    return cnt


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        [
            "********  ",
            "******** ",
            "*R******     ",
            "********   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            49
        ],
        [
            "********  ",
            "******** ",
            "******B*     ",
            "********   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            54
        ],
        [
            "********  ",
            "*R****** ",
            "********     ",
            "*****B**   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            40
        ],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)