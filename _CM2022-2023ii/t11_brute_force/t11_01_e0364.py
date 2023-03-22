length: int
aim: int
alphabet: list
no: int


def solve(word):
    global no
    if len(word) == length:
        no += 1
        return word

    for letter in alphabet:
        if letter not in word:
            result = solve(word + letter)
            if no == aim:
                return result


if __name__ == "__main__":
    N, k = map(int, input().split())

    length = N
    aim = k
    alphabet = [chr(ord("a") + i) for i in range(N)]
    no = 0

    print(solve(""))
