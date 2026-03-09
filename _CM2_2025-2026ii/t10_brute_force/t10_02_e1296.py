max_product: int = 0


def solve(nums: str, pieces: int, value: int):
    # print(nums, pieces, value)
    global max_product
    product = value * int(nums)
    if product < max_product:
        return
    elif pieces == 1:
        max_product = product
        return

    for i in range(1, len(nums) - pieces + 2):
        sub_value = value * int(nums[:i])
        sub_nums = nums[i:]
        solve(sub_nums, pieces - 1, sub_value)


if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        n, m = line.split()
        max_product = 0
        solve(n, int(m), 1)
        print(max_product)
    f.close()

