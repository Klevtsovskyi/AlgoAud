"""
7
153 168 155 167 155 167 155
165 170
6
189 191 169 190 192 191
165 172

3
1
"""


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        while line:
            n = int(line)
            array = list(map(int, f.readline().split()))
            a, b = [int(s) for s in f.readline().split()]
            # print(n, array, a, b)
            line = f.readline().strip()
