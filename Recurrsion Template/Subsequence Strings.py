# recurrence: f(i) represents array of all possible subsequence for the substring s[0:i+1]
# recurrence relation: f(i) = [append s[i] to all the elements of f(i-1)] and [all elements of f(i-1)]
# input i >= 0
def subsequence_strings(s, i):
    # Base Case
    if i < 0:
        return [""]  # Return a list with an empty string as the only subsequence

    # Recurrence relation
    prev_subsequences = subsequence_strings(s, i - 1)
    current_char = s[i]
    
    # Append current character to all previous subsequences
    new_subsequences = [subseq + current_char for subseq in prev_subsequences]
    
    # Combine previous subsequences with new ones
    return prev_subsequences + new_subsequences

# Example usage
if __name__ == "__main__":
    s = "aba"  # Change this string to compute subsequences for a different string
    n = len(s) - 1  # Last index of the string
    print(f"All subsequences of '{s}' are: {subsequence_strings(s, n)}")