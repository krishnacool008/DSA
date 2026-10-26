# recurrence: f(i) represents max coins we have after robbing ith house
# recurrence relation: f(i) = max(f(i-1), f(i-2) + nums[i])
# input i >= 0
def rob(i: int, nums: list) -> int:
    if i < 0:
        return 0
    return max(rob(i - 1, nums), rob(i - 2, nums) + nums[i])

# Example usage:
nums = [2, 7, 9, 3, 1]
result = rob(len(nums) - 1, nums)
print(result)  # Output: 12