max_product: int = 0


def solve(num: str, value: int, pieces: int):
    global max_product
    # print(num, value, pieces)

    product = value * int(num)
    if product < max_product:
        return
    elif pieces == 1:
        max_product = product
        return

    for i in range(1, len(num) - pieces + 2):
        sub_num = num[i:]
        sub_value = value * int(num[:i])
        solve(sub_num, sub_value, pieces - 1)


if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        n, m = line.split()
        max_product = 0
        solve(n, 1, int(m))
        print(max_product)
    f.close()
