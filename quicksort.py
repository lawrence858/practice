from random import randint

comparison_count = 0


def quicksort(arr, start_index, end_index):
    if end_index <= start_index:
        return
    pivot_index = partition(arr, start_index, end_index)
    quicksort(arr, start_index, pivot_index - 1)
    quicksort(arr, pivot_index + 1, end_index)
    return arr


def partition(arr, start_index, end_index):
    global comparison_count
    # use the last element as the pivot
    # initialize left and right pointers
    left_index = start_index - 1
    right_index = start_index

    while right_index <= end_index:
        comparison_count += 1
        # compare with the pivot element
        # eventually right_index == end_index (pivot), and this comparison will be true, moving the pivot element to the left_index
        if arr[right_index] <= arr[end_index]:
            left_index += 1
            swap(arr, left_index, right_index)
        right_index += 1
    return left_index


def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


if __name__ == "__main__":
    arr_len = 100
    arr = [randint(0, 99) for i in range(arr_len)]
    print("input:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("sorted: ", arr)

    print ("element comparison count =", comparison_count)
