# Recurrence: f(i) represents number of ways to reach ith stair from the ground
# Recurrence Relation: f(i) = f(i-1) + f(i-2)
# Constraints: 1 <= i <= 45
def countWays(i):
    # Base Case
    if i <= 1:
        return 1
    else:
        # Recurrence Relation
        return countWays(i - 1) + countWays(i - 2)


# Example usage:
n = 6  # Number of stairs
ways = countWays(n)
print(f"Number of ways to reach the {n}th stair: {ways}")