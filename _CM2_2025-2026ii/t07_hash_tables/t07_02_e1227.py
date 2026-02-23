if __name__ == '__main__':
    # f = open("input.txt")
    words = set()
    # for line in f:
    while True:
        word = ""
        try:
            line = input()
        except EOFError:
            break
        for c in line:
            if c.isalpha():
                word += c.lower()
            elif word:
                words.add(word)
                word = ""
        if word:
            words.add(word)

    print(*sorted(words), sep="\n")
    # f.close()
