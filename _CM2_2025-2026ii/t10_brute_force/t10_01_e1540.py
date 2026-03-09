def solve(lst: list[int]) -> bool:
    for i in range(len(lst)):
        sub_lst = lst[:i] + lst[i + 1:]
        if _solve(sub_lst, lst[i]):
            return True
    return False


def _solve(lst: list[int], value: int) -> bool:
    if len(lst) == 0:
        return value == 23

    for i in range(len(lst)):
        sub_lst = lst[:i] + lst[i + 1:]
        if _solve(sub_lst, value + lst[i]):
            return True
        if _solve(sub_lst, value - lst[i]):
            return True
        if _solve(sub_lst, value * lst[i]):
            return True


if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        lst = [int(x) for x in line.split()]
        if lst == [0, 0, 0, 0, 0]:
            break

        if solve(lst):
            print("Possible")
        else:
            print("Impossible")
    f.close()