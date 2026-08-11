
# Recurrence relation: f(i) = f(i-1) + f(i-2) (This is example of recurrence relation, you can change it according to your problem statement)
def f(i):
    # Base Case
    # Below is example of base case, you can change it according to your problem statement
    if i < 2:
        return i

    # Recurrence relation
    # Below is example of recurrence relation, you can change it according to your problem statement
    return f(i-1) + f(i-2)



# Final Solution function which will call the recursive function f(i) and return the final answer
n = 6  # Example input, you can change it according to your problem statement
result = f(n)