from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

    dfs(0)
    return result


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    subset = []

    def dfs(i):
        subset.append(i)

        if (target - i) in candidates:
            dfs(target - i)
        else:
            result.append(subset.copy())
            subset.clear()
            return

    for item in candidates:
        dfs(item)

    return result


print(combinationSum([2, 3, 6, 7], 7))


#  def dfs(i)
#         subset.append(i)

#         if target - i in List:
#             dfs(target - i)
#         else:
#             result.append(subset.copy())
#             subset = []
#             return

#     for item in candidates:
#         dfs(item)

#     return result
