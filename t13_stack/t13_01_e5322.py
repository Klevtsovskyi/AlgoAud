"""
https://www.eolymp.com/uk/submissions/10951042
"""


def convert(number: str, from_base: int, to_base: int):

    decimal = 0
    for d in number:
        decimal = from_base * decimal + int(d, from_base)

    stack = []

    while decimal > 0:
        stack.append(decimal % to_base)
        decimal //= to_base

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
