

max_value = 0


def arithmetic_masha(product: int, number: str, m: int):
    global max_value

    value = product * int(number)
    if value < max_value:
        return
    if m == 1:
        if value > max_value:
            max_value = value
        return

    for i in range(1, len(number) - m + 2):
        sub_product = product * int(number[:i])
        sub_number = number[i:]
        arithmetic_masha(sub_product, sub_number, m - 1)


if __name__ == '__main__':
    with open("input.txt") as inp:
        for line in inp:
            n, m = line.split()
            max_value = 0
            arithmetic_masha(1, n, int(m))
            print(max_value)
