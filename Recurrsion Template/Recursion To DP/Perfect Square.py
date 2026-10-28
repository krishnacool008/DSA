def perfectSquare(i: int) -> int:
  # Base Cases:
  if i == 0:
    return 0
  if i < 0:
    return float('inf')

  # To keep track of the minimum result
  min_Result = float('inf')

  # Recurrence: 1 + min { f(i - n²) } for all n² such that 0 <= i - n²
  for n in range(1, int(i**0.5) + 1):
    result = 1 + perfectSquare(i - n * n)
    min_Result = min(min_Result, result)

  return min_Result


# Example usage:
print(perfectSquare(12))  # Output: 3