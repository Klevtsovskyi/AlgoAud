# 2 -> 0 1
# 10011 -> 1*2^0 + 1*2^1 + 0*2^2 + 0*2^3 + 1*2^4 = 19
# 1 + 2(1 + 2(0 + 2(0 + 2(1))))
# 19 // 2 = 9, 19 % 2 = 1
# 9 // 2 = 4, 9 % 2 = 1
# 4 // 2 = 2, 4 % 2 = 0
# 2 // 2 = 1, 2 % 2 = 0
# 1 // 2 = 0, 1 % 2 = 1

# 3 -> 0 1 2
# 1021 -> 1*3^0 + 2*3^1 + 0*3^2 + 1*3^3 = 34

# 10 -> 0 1 ... 9
# 11 -> 0 1 ... 9 A

# 16 -> 0 1 ... 9 A B C D E F
# 1F -> F*16^0 + 1*16^1 = 15*16^0 + 1*16^1 = 31
# 31 // 16 = 1, 31 % 16 = 15 = F
# 1 // 16 = 0, 1 % 16 = 1


def convert(number: str, from_base: int, to_base: int):
    decimal = 0
    for d in number:
        decimal = decimal * from_base + int(d, from_base)

    stack = []
    while decimal > 0:
        d = decimal % to_base
        decimal //= to_base
        stack.append(d)

    result = ""
    while stack:
        result += get_char(stack.pop())
    return result


def get_char(d: int):
    if d < 10:
        return str(d)
    else:
        return chr(ord("A") + d - 10)


if __name__ == "__main__":
    print(convert(input(), 2, 16))
