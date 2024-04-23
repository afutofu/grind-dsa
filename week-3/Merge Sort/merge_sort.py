def merge_sort(arr) -> list[int]:
    # Implement merge sort
    n: int = len(arr)

    if n == 1:
        return arr

    arr1 = merge_sort(arr[: n // 2])
    arr2 = merge_sort(arr[n // 2 :])

    return merge(arr1, arr2)


def merge(arr1, arr2) -> list[int]:
    # Implement merge function

    sorted_arr = []

    # Compare the first elements of arr1 and arr2 and append the smaller one to the sorted_arr
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            sorted_arr.append(arr1.pop(0))
        else:
            sorted_arr.append(arr2.pop(0))

    # At this point, either arr1 or arr2 is empty
    # If there are elements left in arr1 or arr2, append them to the sorted_arr
    while arr1:
        sorted_arr.append(arr1.pop(0))
    while arr2:
        sorted_arr.append(arr2.pop(0))

    return sorted_arr


if __name__ == "__main__":

    # Test the merge sort implementation with dummy list
    # Test the merge sort implementation with dummy list
    dummy_list = [4, 2, 7, 1, 9, 5]
    print("Dummy list is")
    for i in range(len(dummy_list)):
        print("%d" % dummy_list[i], end=" "),

    sorted_arr_1: list[int] = merge_sort(dummy_list)
    print("\nSorted dummy list is")
    for i in range(len(dummy_list)):
        print("%d" % sorted_arr_1[i], end=" "),

    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("\nGiven array is")
    for i in range(n):
        print("%d" % arr[i], end=" "),

    sorted_arr_2: list[int] = merge_sort(arr)
    print("\nSorted array is")
    for i in range(n):
        print("%d" % sorted_arr_2[i], end=" "),
