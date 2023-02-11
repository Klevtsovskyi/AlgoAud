#!/usr/bin/env python
# -*- coding: utf-8 -*-

import user as user


def main(input_file):
    _lst = []
    error = 0
    test_num = 0

    user.init()
    _cur = -1

    with open(input_file) as f_in:
        for line in f_in:
            pair = line.strip().split()

            if len(pair) != 1 and len(pair) != 2:
                continue

            key = pair[0]
            item = 0
            if len(pair) == 2:
                item = int(pair[1])

            if key == "empty":
                test_num += 1
                out_empty = user.empty()
                lst_empty = len(_lst) == 0
                if out_empty != lst_empty:
                    error += 1

            elif key == "set_first":
                if len(_lst) == 0:
                    continue

                _cur = 0
                user.set_first()

            elif key == "set_last":
                if len(_lst) == 0:
                    continue

                _cur = len(_lst) - 1
                user.set_last()

            elif key == "next":
                test_num += 1

                if len(_lst) == 0:
                    try:
                        user.next()
                    except StopIteration:
                        pass
                    else:
                        error += 1
                    continue

                if _cur == len(_lst) - 1:
                    try:
                        user.next()
                        error += 1
                    except StopIteration:
                        pass
                    continue

                _cur += 1
                try:
                    user.next()
                except StopIteration:
                    error += 1

            elif key == "prev":
                test_num += 1

                if len(_lst) == 0:
                    try:
                        user.prev()
                    except StopIteration:
                        pass
                    else:
                        error += 1
                    continue

                if _cur == 0:
                    try:
                        user.prev()
                        error += 1
                    except StopIteration:
                        pass
                    continue

                _cur -= 1
                try:
                    user.prev()
                except StopIteration:
                    error += 1

            elif key == "current":
                if len(_lst) == 0:
                    continue

                test_num += 1
                out_current = user.current()
                lst_current = _lst[_cur]
                if out_current != lst_current:
                    error += 1

            elif key == "insert_after":
                _lst.insert(_cur + 1, item)
                user.insert_after(item)
                if len(_lst) == 1:
                    _cur = 0

            elif key == "insert_before":
                _lst.insert(_cur, item)
                user.insert_before(item)
                if len(_lst) == 1:
                    _cur = 0
                else:
                    _cur += 1

            elif key == "delete":
                if len(_lst) == 0:
                    continue

                user.delete()
                _lst.pop(_cur)
                if _cur == len(_lst):
                    _cur = len(_lst) - 1

        score = 100 * (test_num - error) / test_num
        return score if score > 40 else 0


if __name__ == "__main__":
    res1 = main("input01.txt")
    print("Score 1: %d%%" % res1)
    res2 = main("input02.txt")
    print("Score 2: %d%%" % res2)
    res3 = main("input03.txt")
    print("Score 3: %d%%" % res3)
    res4 = main("input04.txt")
    print("Score 4: %d%%" % res4)
    res5 = main("input05.txt")
    print("Score 5: %d%%" % res5)
