def characterReplacement(s: str, k: int) -> int:
    char_count = {}
    left = 0
    max_length = 0
    max_count = 0

    for right in range(len(s)):

        # Increase right pointer to expand the window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])

        # Check if window is valid, if not then keep shrinking the window from the left
        # Until it is valid again
        while (right - left + 1) - max_count > k:
            # When decreasing the count we are not interested in the max_count as 
            # Once we have the max_count the answer will always have that max_count or greater than that, 
            # so we can just ignore the max_count when we are decreasing the count
            char_count[s[left]] -= 1
            left += 1

        # Keep the max length of the window we have seen so far
        max_length = max(max_length, right - left + 1)

    # Return the max length of the window
    return max_length


# Example usage:
s = "AAABABB"
k = 1
print(characterReplacement(s, k))