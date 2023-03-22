DRAW = 0
FIRST = 1
SECOND = 2

size = 0
OO = "O"
XX = "X"


def play(field: str, turn):
    # print(field, turn)
    i = -1
    while True:
        i = field.find(OO, i + 1)
        if i == -1:
            break
        sub_field = field[:i] + XX + field[i + size:]
        sub_turn = SECOND if turn == FIRST else FIRST
        if play(sub_field, sub_turn) == turn:
            return turn

    return SECOND if turn == FIRST else FIRST


if __name__ == "__main__":
    with open("input.txt") as f:
        n, k = map(int, f.readline().split())
        string = f.readline().strip()

        size = k
        OO *= size
        XX *= size

        if string.find(OO) == -1:
            print(DRAW)
        else:
            print(play(string, FIRST))
