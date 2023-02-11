"""
https://www.eolymp.com/uk/submissions/10914839
"""


max_income = 0


def the_vouchers(income, lst, day):
    global max_income
    # print(income, lst, day)
    if len(lst) == 0 and income > max_income:
        max_income = income

    for i in range(len(lst)):
        sub_income = income + lst[i][1] * (lst[i][0] - day)
        sub_lst = []
        for j in range(len(lst)):
            if j == i or lst[j][0] <= day + 1:
                continue
            sub_lst.append(lst[j])

        the_vouchers(sub_income, sub_lst, day + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())

        vouchers = []
        for _ in range(n):
            vouchers.append(
                tuple(int(k) for k in f.readline().split())
            )

        # print(vouchers)
        the_vouchers(0, vouchers, 0)
        print(max_income)
