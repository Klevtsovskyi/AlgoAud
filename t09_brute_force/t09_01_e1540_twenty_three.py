

def _tt(value, numbers):
    if len(numbers) == 0:
        return value == 23

    for i in range(len(numbers)):
        sub_numbers = numbers[:i] + numbers[i + 1:]
        for operation in ("+", "-", "*"):
            if operation == "+":
                sub_value = value + numbers[i]
            elif operation == "-":
                sub_value = value - numbers[i]
            elif operation == "*":
                sub_value = value * numbers[i]

            if _tt(sub_value, sub_numbers):
                return True

    return False


def twenty_three(numbers):
    for i in range(len(numbers)):
        sub_value = numbers[i]
        sub_numbers = numbers[:i] + numbers[i + 1:]
        if _tt(sub_value, sub_numbers):
            return True
    return False


if __name__ == '__main__':
    with open("input.txt") as inp:
        data = [int(s) for s in inp.readline().split()]
        while any(data):
            result = twenty_three(data)
            print("Possible" if result else "Impossible")
            data = [int(s) for s in inp.readline().split()]
