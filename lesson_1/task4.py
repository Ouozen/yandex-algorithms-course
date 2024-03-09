from unittest.mock import patch
from tqdm import tqdm


def algorithm() -> int:
    figures = {
        "R": [ # ладья
            [],
            [0, -1], [1, 0], [0, 1], [-1, 0] # паттерн перемещения
        ],
        "B": [ # слон
            [],
            [1, 1], [-1, -1], [1, -1], [-1, 1] # паттерн перемещения
        ],
    }
    cnt = 64
    for row in range(8):
        line = list(input().strip())
        while "R" in line:
            column = line.index("R")
            figures["R"][0].append([row, column])
            line[column] = "*"
        while "B" in line:
            column = line.index("B")
            figures["B"][0].append([row, column])
            line[column] = "*"

    coord_figures = figures["R"][0].copy()
    coord_figures.extend(figures["B"][0])
    list_coord = []

    for figure, coord_list in figures.items():
        coords = coord_list[0]
        pattern = coord_list[1:]
        for x_fig, y_fig in coords:
            cnt -= 1 # удаляем фигуру которую сейчас исследуем
            for x_mul, y_mul in pattern:
                step = True
                step_plus = 1
                while step:
                    x_now = x_fig + step_plus * x_mul
                    y_now = y_fig + step_plus * y_mul

                    if [x_now, y_now] in coord_figures:
                        step = False
                        continue

                    if x_now > 7 or x_now < 0 or y_now > 7 or y_now < 0:
                        step = False
                    elif [x_now, y_now] in list_coord:
                        pass
                    else:
                        cnt -= 1
                        list_coord.append([x_now, y_now])

                    step_plus += 1
    return cnt


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        [ # 1
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
        [ # 2
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
        [ # 3
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
        [ # 4
            "R*******  ",
            "******** ",
            "********     ",
            "********   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            49
        ],
        [ # 5
            "B*******  ",
            "******** ",
            "********     ",
            "********   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            56
        ],
        [ # 6
            "********  ",
            "******** ",
            "********     ",
            "****B***   ",
            "****R***  ",
            "********",
            "********",
            "********",
            "",
            "",
            41
        ],
        [ # 7
            "R*******  ",
            "*B****** ",
            "********     ",
            "********   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            42
        ],
        [ # 8
            "********  ",
            "*R*****B ",
            "********     ",
            "********   ",
            "********  ",
            "********",
            "********",
            "********",
            "",
            "",
            43 # [1,7]
        ],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)