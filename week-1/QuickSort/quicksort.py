import random
from datetime import datetime


def quicksort(arr) -> int:
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    pivot = arr.pop()
    while arr:
        el = arr.pop()
        if el < pivot:
            left.append(el)
        else:
            right.append(el)

    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    arr = []

    for i in range(100000):
        arr.append(random.randint(0, 10000))

    sorted_arr_start = datetime.utcnow()
    sorted_arr = sorted(arr)
    sorted_arr_end = datetime.utcnow()
    sorted_arr_time = sorted_arr_end - sorted_arr_start

    qsorted_arr_start = datetime.utcnow()
    qsorted_arr = quicksort(arr)
    qsorted_arr_end = datetime.utcnow()
    qsorted_arr_time = qsorted_arr_end - qsorted_arr_start

    print(sorted_arr_time)
    print(qsorted_arr_time)
    print(sorted_arr == qsorted_arr)
