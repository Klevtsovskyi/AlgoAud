DRAW = 0
FIRST = 1
SECOND = 2

k: int  # розмір блоку, який треба закреслювати
OO = "O"
XX = "X"


def solve(field: str, turn: [FIRST | SECOND]) -> [FIRST | SECOND]:
    # print(field, turn)
    i = -1
    while True:
        i = field.find(OO, i + 1)
        if i == -1:
            break
        sub_field = field[:i] + XX + field[i + k:]
        sub_turn = FIRST if turn == SECOND else SECOND
        if solve(sub_field, sub_turn) == turn:
            return turn

    return FIRST if turn == SECOND else SECOND


if __name__ == '__main__':
    n, k = map(int, input().split())
    field = input()

    OO *= k
    XX *= k
    if field.find(OO) == -1:
        print(DRAW)
    else:
        print(solve(field, FIRST))
