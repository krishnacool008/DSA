
def combinationSum(nums, target):
    nums.sort(reverse=True)
    results = []

    def backtracking(index, path, currentSum):
        if currentSum == target:
            results.append(path[:])
            return

        if currentSum > target:
            return

        # i will start from current index plus move forward till len
        for i in range(index, len(nums)):  # ← uses index to control which num can be used
            num = nums[i]
            path.append(num)
            print(path)
            backtracking(i, path, currentSum + num)  # reuse allowed
            path.pop()

    backtracking(0, [], 0)
    return results


nums = [2,5,6,9] 
t = 9
print(combinationSum(nums, t))