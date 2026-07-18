from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

        def backtrack(start, path):
            # Append the current subset to the result
            # We want all possible subset so all case are accepted no need for if statement
            result.append(path[:])  # Make a copy of the current path
            
            # Iterate through the remaining elements
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])
                # Move forward to the next element
                backtrack(i + 1, path)
                # Backtrack: remove the last element before moving to the next
                path.pop()
    
        result = []
        backtrack(0, [])
        return result

# Example usage:
nums = [1,2,3]
print(subsets(nums))
