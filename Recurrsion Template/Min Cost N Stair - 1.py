# Recurrence: f(i) represents Min cost to reach ith stair and use ith stair
# Recurrence Relation: f(i) = min( f(i-1) , f(i-2) ), cost[i]
def minCost(i: int, cost: list) -> int:
    if i <=1 :
        return cost[i]
    else:
        return min(minCost(i-1, cost), minCost(i-2, cost)) + cost[i]


# Example usage
if __name__ == "__main__":
    cost = [10, 15, 20]  # Example input, you can change it according to your problem statement
    n = len(cost) - 1
    print(f"The minimum cost to reach the top of the stairs is: {minCost(n, cost)}")
    