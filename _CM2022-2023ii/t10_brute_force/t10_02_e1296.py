max_value = 0


def solve(nums, pieces, value):
    global max_value

    product = int(nums) * value
    if product < max_value:
        return
    elif pieces == 1:
        max_value = product
        return

    for i in range(1, len(nums) - pieces + 2):
        solve(nums[i:], pieces - 1, value * int(nums[:i]))


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            n, m = line.split()
            max_value = 0
            solve(n, int(m), 1)
            print(max_value)
