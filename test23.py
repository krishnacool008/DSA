def minCoin(nums, target):
    nums.sort(reverse=True)
    minLength = [float('inf')]

    def backtracking(index, path, currentSum):
        if currentSum == target:
            minLength[0] = min(minLength[0], len(path))
            return
        
        if currentSum > target or len(path) >= minLength[0]:
            return

        # This forloops remains same for each backtrack call
        # We not starting from and index 
        # We will alaways iterate over all the coins in nums
        for coin in nums:  # ← iterates over *values*, not indices
            path.append(coin)
            print(path)
            backtracking(coin, path, currentSum + coin)  # ← passes a *value*, not an index!
            path.pop()

    backtracking(0, [], 0)
    return minLength[0] if minLength[0] != float('inf') else -1

k = [5,1,2]
t = 11
print(minCoin(k, t))
