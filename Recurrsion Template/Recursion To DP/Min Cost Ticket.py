def minCostTicket(i: int, days: list, costs: list) -> int:
    if i >= len(days):
        return 0

    # Day Pass Coverage: 1 day
    day_pass = costs[0] + minCostTicket(i+1, days, costs)
    
    # Week Pass Coverage: 7 days
    n7 = 0
    for n in range(i, len(days)):
        if days[n] > days[i] + 6:
            n7 = n
            break
    week_pass = costs[1] + minCostTicket(n7, days, costs)

    # Month Pass Coverage: 30 days
    n30 = 0
    for n in range(i, len(days)):
        if days[n] > days[i] + 29:
            n30 = n
            break
    month_pass = costs[2] + minCostTicket(n30, days, costs)

    return min(day_pass, week_pass, month_pass)


# Example usage:
days = [1,4,6,7,8,20]
costs = [2,7,15]

print(minCostTicket(0, days, costs))  # Output: 11