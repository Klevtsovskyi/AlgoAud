"""
https://www.eolymp.com/uk/submissions/10903704
"""


max_value = 0


def masha(value: int, number: str, pieces: int):
    global max_value

    product = value * int(number)
    if product < max_value:
        return
    elif pieces == 1:
        max_value = product
        return

    for i in range(1, len(number) - pieces + 2):
        sub_value = value * int(number[:i])
        sub_number = number[i:]
        masha(sub_value, sub_number, pieces - 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            n, m = line.split()
            max_value = 0
            masha(1, n, int(m))
            print(max_value)
