

def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    stack = [(0, len(array) - 1)]
    while stack:
        a, b = stack.pop()

        if a >= b:
            continue

        pivot = array[a]
        l = a
        r = b
        while True:
            while array[l] < pivot:
                l += 1
            while array[r] > pivot:
                r -= 1

            if l >= r:
                break

            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

        stack.append((a, r))
        stack.append((r + 1, b))
