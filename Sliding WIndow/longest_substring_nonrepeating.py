def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0 # We us left pointer to remove the character form seen
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):

        # If we seen current right pointer character
        # We remove character from seen using left pointer until the current character
        # Become unseen
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Now the character at right pointer is unseen, we add it to the seen set 
        char_set.add(s[right])

        # Update the maximum length of substring without repeating characters
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "zxyzxyz"
print(lengthOfLongestSubstring(s))