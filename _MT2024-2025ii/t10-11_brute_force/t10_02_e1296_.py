max_value: int = 0


def solve(num: str, pieces: int, value: int):
    global max_value
    product = int(num) * value
    if product <= max_value:
        return
    elif pieces == 1:
        max_value = product
        return

    for i in range(1, len(num) - pieces + 2):
        sub_num = num[i:]
        sub_value = int(num[:i]) * value
        solve(sub_num, pieces - 1, sub_value)


if __name__ == "__main__":
    f = open("input.txt")
    for line in f:
        n, m = line.split()
        max_value = 0
        solve(n, int(m), 1)
        print(max_value)
    f.close()
