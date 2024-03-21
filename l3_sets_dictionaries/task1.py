from unittest.mock import patch

from tqdm import tqdm


def algorithm():
    N = int(input())
    all_tracks = dict()
    for _ in range(N):
        K = int(input())
        like_tracks = list(input().split(' '))
        for i in like_tracks:
            all_tracks[i] = all_tracks.get(i, 0) + 1

    list_result_track = list()
    for key, item in all_tracks.items():
        if item == N:
            list_result_track.append(key)

    result_tracks = sorted(list_result_track)
    return str(len(result_tracks)) + ' ' + ' '.join(result_tracks)


def test_algorithm(*args):
    with patch("builtins.input", side_effect=[*args[:-1]]):
        test_answer = algorithm()
        # print(test_answer)
        assert test_answer == args[-1]


if __name__ == "__main__":
    test_case = [
        ['1', '2', 'GoGetIt Life', '2 GoGetIt Life'],
        ['2', '2', 'Love Life', '2', 'Life GoodDay', '1 Life'],
    ]
    for case in tqdm(test_case):
        test_algorithm(*case)