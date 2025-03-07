max_income: int = 0


def solve(income: int, vouchers: list[tuple], day) -> None:
    global max_income
    # print(income, vouchers, day)
    if len(vouchers) == 0 and income > max_income:
        max_income = income

    for i in range(len(vouchers)):
        sub_income = (vouchers[i][0] - day) * vouchers[i][1] + income
        sub_vouchers = []
        for j in range(len(vouchers)):
            if i != j and vouchers[j][0] - day > 1:
                sub_vouchers.append(vouchers[j])
        solve(sub_income, sub_vouchers, day + 1)


if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        vouchers = []
        for _ in range(n):
            vouchers.append(
                tuple(map(int, f.readline().split()))
            )
        solve(0, vouchers, 0)
        print(max_income)
