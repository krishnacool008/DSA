# recurrence: f(i) represents number at ith position of tribunacci series
# recurrence relation: f(i) = f(i-1) + f(i-2) + f(i-3)
# input i >= 0
def tribunacchi(i):
    # Base Case
    if i < 2:
        return i
    elif i == 2:
        return 1

    # Recurrence relation
    return tribunacchi(i-1) + tribunacchi(i-2) + tribunacchi(i-3)

# Example usage
if __name__ == "__main__":
    n = 10  # Change this value to compute a different Tribonacci number
    print(f"The {n}th Tribonacci number is: {tribunacchi(n)}")