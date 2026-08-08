# recurrence relation: f(i) = f(i-1) + f(i-2)
# input i >= 0
def fibonacchi(i):
    if i < 2:
        return i
    return fibonacchi(i-1) + fibonacchi(i-2)


# Example usage
if __name__ == "__main__": 
    n = 10  # Change this value to compute a different Fibonacci number
    print(f"The {n}th Fibonacci number is: {fibonacchi(n)}")