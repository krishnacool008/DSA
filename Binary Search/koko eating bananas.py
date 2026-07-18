from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:

    # Helper function to check if Koko can eat all bananas at a given speed within h hours
    def canEatAll(speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Equivalent to math.ceil(pile / speed)
        return hours <= h

    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2
        if canEatAll(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

# Example usage:
piles = [1,4,3,2]
h = 9
print(minEatingSpeed(piles, h))  # Output: 4