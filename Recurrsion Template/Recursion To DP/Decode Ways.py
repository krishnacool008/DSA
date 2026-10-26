def decodeWays(i: int, s: str) -> int:
    #Base Cases:
    if i < 0:
        return 1
    if i == 0:
        return 0 if (s[0] == '0') else 1
    

    # Recurrence: f(i) = f(i-1) + f(i-2)
    contribution1 = decodeWays(i - 1, s) if (s[i] != '0') else 0
    contribution2 = decodeWays(i - 2, s) if ( 10 <= (int(s[i - 1:i + 1])) <= 26) else 0
    result = contribution1 + contribution2
    return result


# Example usage:
s = "10"
lastIndex = len(s) - 1

if not s or s[0] == '0':
    print(0)  # Output: 0
else:
    result = decodeWays(lastIndex, s)
    print(result)  # Output: 2