def _solve(nums, value):
    if len(nums) == 0:
        return value == 23

    for i in range(len(nums)):
        sub_nums = nums[:i] + nums[i + 1:]
        if _solve(sub_nums, value + nums[i]):
            return True
        if _solve(sub_nums, value - nums[i]):
            return True
        if _solve(sub_nums, value * nums[i]):
            return True


def solve(nums):
    for i in range(len(nums)):
        if _solve(nums[:i] + nums[i + 1:], nums[i]):
            return True


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            numbers = list(map(int, line.split()))
            if not any(numbers):
                break
            print("Possible" if solve(numbers) else "Impossible")

