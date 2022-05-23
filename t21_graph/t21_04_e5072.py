"""
https://www.eolymp.com/uk/submissions/11104059
"""


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        count = 0
        for _ in range(n):
            count += sum(int(k) for k in f.readline().split())
        print(count)
