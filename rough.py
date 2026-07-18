def combination_sum2(candidates, target):
    def backtrack(start, total, path):
        # Base case: if the total equals the target, add the current combination to the results
        if total == target:
            result.append(path[:])
            return

        # If the total exceeds the target, stop recursion
        if total > target:
            return

        for i in range(start, len(candidates)):
            # Include the current number and move to the next
            path.append(candidates[i])
            backtrack(i + 1, total + candidates[i], path)
            path.pop()  # Backtrack by removing the last added number

    # Remove duplicates and sort the array
    candidates = sorted(set(candidates))
    result = []
    backtrack(0, 0, [])
    return result

# Example usage:
candidates = [2,2,4,4,5]
target = 8
print(combination_sum2(candidates, target))
