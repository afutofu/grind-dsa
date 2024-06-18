def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    target = 3
    print(binarySearch(arr, target))  # 1

    arr = [1, 3, 5, 7, 9]
    target = 2
    print(binarySearch(arr, target))  # -1

    arr = [1, 3, 5, 7, 9]
    target = 9
    print(binarySearch(arr, target))  # 4

    arr = [1, 3, 5, 7, 9]
    target = 1
    print(binarySearch(arr, target))  # 0
