# 11001 = 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0 =
# ((((1) * 2 + 1) * 2 + 0) * 2 + 0) * 2 + 1 =

def convert(number: str, from_base=2, to_base=16) -> str:
    decimal = 0
    for d in number:
        decimal = decimal * from_base + int(d, from_base)
    # print(decimal)
    stack = []
    while decimal > 0:
        d = decimal % to_base
        decimal = decimal // to_base
        stack.append(d)

    result = ""
    while stack:
        result += get_char(stack.pop())
    return result


def get_char(n: int) -> str:
    if n < 10:
        return str(n)
    else:
        return chr(ord("A") + n - 10)


if __name__ == '__main__':
    num = input()
    res = convert(num, 2, 16)
    print(res)
