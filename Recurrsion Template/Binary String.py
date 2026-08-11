# recurrence: f(i) represents array of all possible binary strings of length i
# recurrence relation: f(i) = [append '0' to all the elements of f(i-1)] and [append '1' to all the elements of f(i-1)]
# input i >= 0
def binary_strings(i):
    # Base Case
    if i == 0:
        return [""]  # Return a list with an empty string as the only binary string of length 0

    # Recurrence relation
    prev_binary_strings = binary_strings(i - 1)
    
    # Append '0' and '1' to all previous binary strings
    new_binary_strings = [s + '0' for s in prev_binary_strings] + [s + '1' for s in prev_binary_strings]
    
    return new_binary_strings

# Example usage
if __name__ == "__main__":
    length = 3  # Change this value to compute binary strings of a different length
    print(f"All binary strings of length {length} are: {binary_strings(length)}")