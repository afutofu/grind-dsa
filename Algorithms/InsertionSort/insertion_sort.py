def insertion_sort(arr):
    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element
        j = i - 1  # Initialize a pointer to the previous element

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1  # Move the pointer to the left

        # Insert the key at its correct position in the sorted subarray
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(insertion_sort(arr))  # [5, 6, 11, 12, 13]

    arr = [1, 3, 5, 7, 9]
    print(insertion_sort(arr))  # [1, 3, 5, 7, 9]

    arr = [9, 7, 5, 3, 1]
    print(insertion_sort(arr))  # [1, 3, 5, 7, 9]

    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(insertion_sort(arr))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
