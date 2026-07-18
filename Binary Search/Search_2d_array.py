from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        # right - left / 2 will give us middle value of left and right pointer
        # Now we are starting from left pointer so we offset the mid value by left pointer.
        # Doing this instead of (left + right) // 2 to avoid integer overflow in some languages.
        mid = left + (right - left) // 2

        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example usage:
matrix = [
    [1,2,4,8],
    [10,11,12,13],
    [14,20,30,40]
    ]

target = 21

print(searchMatrix(matrix, target))# Output: True