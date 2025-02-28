max_value = 0


def solve(nums: str, pieces: int, value: int):
    global max_value
    # print(nums, pieces, value)
    product = value * int(nums)
    if product < max_value:
        return
    elif pieces == 1:
        max_value = product
        return

    for i in range(1, len(nums) - pieces + 2):
        sub_nums = nums[i:]
        sub_value = value * int(nums[:i])
        solve(sub_nums, pieces - 1, sub_value)


if __name__ == "__main__":
    f = open("input.txt")
    for line in f:
        n, m = line.split()
        max_value = 0
        solve(n, int(m), 1)
        print(max_value)
    f.close()
