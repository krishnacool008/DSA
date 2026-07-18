from typing import List


def BinarySearch(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return nums[mid]

    return -1


def quick_sort_in_place(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, partition_index - 1)
        quick_sort_in_place(arr, partition_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
quick_sort_in_place(my_list, 0, len(my_list) - 1)
print(my_list)
