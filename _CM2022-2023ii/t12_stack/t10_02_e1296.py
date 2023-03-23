def solve(nums, pieces, value):
    max_value = 0
    stack = [(nums, pieces, value)]

    while stack:
        nums, pieces, value = stack.pop()
        # print(nums, pieces, value)
        product = int(nums) * value
        if product < max_value:
            continue
        elif pieces == 1:
            max_value = product
            continue

        for i in range(1, len(nums) - pieces + 2):
            stack.append((nums[i:], pieces - 1, value * int(nums[:i])))

    return max_value


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            n, m = line.split()
            print(solve(n, int(m), 1))
