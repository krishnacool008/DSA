# recurrence: f(i) represents sum of array till ith index including ith item
# recurrence relation: f(i) = f(i-1) + arr[i]
# input i >= 0
def sum_of_array(arr, i):
    # Base Case
    if i == 0:
        return arr[0]

    # Recurrence relation
    return arr[i] + sum_of_array(arr, i - 1)

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # Change this array to compute sum of different elements
    n = len(arr) - 1  # Last index of the array
    print(f"The sum of the array is: {sum_of_array(arr, n)}")