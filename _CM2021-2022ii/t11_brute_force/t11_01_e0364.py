"""
https://www.eolymp.com/uk/submissions/10914742
"""

length = 0
no_find = 0
letters = []
no = 0


def dictionary(word):
    global no
    if len(word) == length:
        no += 1
        # print(word, no)
        return word

    for letter in letters:
        if letter not in word:
            sub_word = word + letter
            result = dictionary(sub_word)
            if no == no_find:
                return result


if __name__ == "__main__":
    n, k = map(int, input().split())

    length = n
    no_find = k
    letters = [chr(ord('a') + i) for i in range(length)]
    no = 0

    print(dictionary(""))
