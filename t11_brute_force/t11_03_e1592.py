"""
https://www.eolymp.com/uk/submissions/10940595
"""


min_time = float("inf")
min_strategy = None


def _move(from_, to_, time, strategy, *indexes):
    strategy.append(
        tuple(sorted(from_[i] for i in indexes))
    )
    time += strategy[-1][-1]
    for i in indexes:
        to_.append(from_.pop(i))
    return from_, to_, time, strategy


def _bridge(left: list, right: list, time: int, strategy: list[tuple]):
    global min_time, min_strategy

    for i in range(1, len(left)):
        for j in range(i):
            sleft, sright, stime, sstrategy = _move(left[:], right[:], time, strategy[:], i, j)

            if stime > min_time:
                return

            if len(sleft) > 0:
                for k in range(len(sright)):
                    ssright, ssleft, sstime, ssstrategy = _move(sright[:], sleft[:], stime, sstrategy[:], k)
                    _bridge(ssleft, ssright, sstime, ssstrategy)
            elif stime < min_time:
                min_time = stime
                min_strategy = sstrategy


def bridge(left):
    global min_time, min_strategy
    min_time = float("inf")
    min_strategy = None

    if len(left) == 0:
        return 0, [()]
    elif len(left) == 1:
        return left[0], [(left[0], )]

    _bridge(left, [], 0, [])
    return min_time, min_strategy


if __name__ == "__main__":
    with open("input.txt") as f:
        while True:
            n = f.readline().strip()
            if n == "":
                break
            left_shore = [int(m) for m in f.readline().split()]
            t, s = bridge(left_shore)
            print(t)
            for move in s:
                print(*move)
