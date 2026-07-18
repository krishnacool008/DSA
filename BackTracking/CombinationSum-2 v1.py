
def combinationSum2(candidates, target):
    candidates.sort(reverse=True)
    results = []

    def backtracking(index, path, currentSum):
        if currentSum == target:
            if path[:] not in results:  # to avoid duplicates
                results.append(path[:])
            return

        if currentSum > target:
            return

        # i will start from current index plus move forward till len
        for i in range(index, len(candidates)):  # ← uses index to control which num can be used
            num = candidates[i]
            path.append(num)
            print(path)
            backtracking(i+1, path, currentSum + num)  # reuse not allowed
            path.pop()

    backtracking(0, [], 0)
    return results

candidates = [9,2,2,4,6,1,5]
target = 8
print(combinationSum2(candidates, target))