def coinChange(i: int, nums: list) -> int:
    min_Result = float('inf')
    #Base Case:
    if i == 0:
        return 0

    # Recurrence: min(1 + f(i-n)) for n in coins where i-n >= 0`
    for n in nums:
        if i - n >= 0:
            result = 1 + coinChange(i - n, nums)
            min_Result = min(min_Result, result)

    return min_Result


# Example usage:
# Result = Inf if target cannot be formed with given coins
nums = [1, 2, 3]
target = 9
result = coinChange(target, nums)
print(result)  # Output: 3