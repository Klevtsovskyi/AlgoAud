

if __name__ == '__main__':
    f = open("input.txt")
    dct = dict()
    for line in f:
        eng, latins = line.strip().split(" - ")
        latins = latins.split(", ")
        for latin in latins:
            if latin in dct:
                dct[latin].append(eng)
            else:
                dct[latin] = [eng]

    print(len(dct))
    latins = sorted(dct.keys())
    for latin in latins:
        print(latin, end=" - ")
        print(*sorted(dct[latin]), sep=", ")
    f.close()
