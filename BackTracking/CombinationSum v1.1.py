
def combinationSum(nums, target):
    nums.sort(reverse=True)
    results = []

    def backtracking(index, path, currentSum):
        if currentSum == target:
            results.append(path[:])
            return
        
        if currentSum > target:
            return

        # This forloops remains same for each backtrack call
        # We not starting from an index 
        # We will alaways iterate over all the num in nums
        for num in nums:  # ← iterates over *values*, not indices
            path.append(num)
            print(path)
            backtracking(num, path, currentSum + num)  # ← passes a *value*, not an index!
            path.pop()

    backtracking(0, [], 0)
    return results

nums = [2,5,6,9] 
t = 9
print(combinationSum(nums, t))