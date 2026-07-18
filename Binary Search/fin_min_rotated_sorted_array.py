from ast import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # We have two cases:
        # We are taking right pointer as anchor because 
        # Right pointer include the minimum element, so we can compare mid with right pointer
        # However left pointer may not include the minimum element, so we cannot compare mid with left pointer
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Example usage:
nums = [5,6,7,8,0,1,2,3,4]
print(findMin(nums))  # Output: 1