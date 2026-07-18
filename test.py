nums = [1,2,4,6]
n = len(nums)
for i in range(n - 1, -1, -1):
    print(f"Index {i} -> {nums[i]}", end=", ")