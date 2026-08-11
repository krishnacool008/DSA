# Recurrence: f(i) represents Min cost to reach the top from ith stair
# Recurrence Relation: f(i) = cost[i] + min( f(i+1), f(i+2) )
def minCost(i: int, cost: list) -> int:
    if i > len(cost) - 1:
        return 0
    else:
        return cost[i] + min( minCost(i + 1, cost), minCost(i + 2, cost) )


# Example usage
if __name__ == "__main__":
    cost = [10, 15, 20]  # Cost to step on each stair
    min_cost = min(minCost(0, cost), minCost(1, cost))
    print(f"Minimum cost to reach the top: {min_cost}")
    