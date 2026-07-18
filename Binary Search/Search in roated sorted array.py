from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            # If target is in this half
            # If yes, we shrink the search space
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            # Discard this half
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # If target is in this half
            # If yes, we shrink the search space
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            # Discard this half
            else:
                right = mid - 1
    
    return -1

nums=[3,4,5,6,1,2]
target=1

print(search(nums, target))