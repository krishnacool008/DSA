def QuickSort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        QuickSort(arr, low, partition_index - 1)
        QuickSort(arr, partition_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    Done = False

    while not Done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            Done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
        
    arr[low], arr[right] = arr[right], arr[low]
    return right


# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
QuickSort(my_list, 0, len(my_list) - 1)
print(my_list)