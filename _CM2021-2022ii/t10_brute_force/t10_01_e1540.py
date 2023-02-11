"""
https://www.eolymp.com/uk/submissions/10903277
"""


def _twenty_three(value: int, numbers: list[int]):

    if len(numbers) == 0:
        return value == 23

    for i in range(len(numbers)):
        sub_numbers = numbers[:i] + numbers[i + 1:]
        if _twenty_three(value + numbers[i], sub_numbers):
            return True
        if _twenty_three(value - numbers[i], sub_numbers):
            return True
        if _twenty_three(value * numbers[i], sub_numbers):
            return True

    return False


def twenty_three(numbers: list[int]):
    for i in range(len(numbers)):
        if _twenty_three(numbers[i], numbers[:i] + numbers[i + 1:]):
            return True
    return False


if __name__ == "__main__":
    with open("input.txt") as f:
        while True:
            data = [int(n) for n in f.readline().split()]
            if not any(data):
                break
            print("Possible" if twenty_three(data) else "Impossible")
