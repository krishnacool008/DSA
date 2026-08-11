# recurrence: f(i) represents x to power i
# recurrence relation: f(i) = f(i-1) * x
# input i >= 0
def power(x, i):
    # Base Case
    if i == 0:
        return 1

    # Recurrence relation
    return x * power(x, i - 1)

# Example usage
if __name__ == "__main__":
    x = 2  # Change this value to compute a different base
    n = 5  # Change this value to compute a different exponent
    print(f"{x} to the power of {n} is: {power(x, n)}")