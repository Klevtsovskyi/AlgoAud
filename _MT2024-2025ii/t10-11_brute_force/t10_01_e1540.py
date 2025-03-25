def solve(nums: list[int]) -> bool:
    for i in range(len(nums)):
        sub_nums = nums[:i] + nums[i + 1:]
        if _solve(sub_nums, nums[i]):
            return True
    return False


def _solve(nums: list[int], value: int) -> bool:
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


if __name__ == "__main__":
    f = open("input.txt")
    for line in f:
        numbers = [int(x) for x in line.split()]
        if numbers == [0, 0, 0, 0, 0]:
            break
        if solve(numbers):
            print("Possible")
        else:
            print("Impossible")
    f.close()

