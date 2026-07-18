from typing import List

def search(nums: List[int], target: int) -> int:

        def binary_search(array, left, right):
            l, r = left , right
            while l <= r:
                mid = (l + r ) // 2
                if target > array[mid]:
                    l = mid + 1
                elif target < array[mid]:
                    r = mid - 1
                else:
                    return mid
            return -1
            
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        if nums[left] <= target <= nums[len(nums) - 1]:
            return binary_search(nums, left, len(nums) - 1)
        else:
            return binary_search(nums, 0, left - 1)
        
nums=[3,4,5,6,1,2]
target=1

print(search(nums, target))
        