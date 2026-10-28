def jumpGame(i: int, jumpp: list) -> int:
  # Base Cases:
  if i == 0:
    return 0
  
  # To keep track of the minimum result
  min_Result = float('inf')

  # Recurrence: 1 + min( f(n) for all n where jumpp[n] >= i - n )
  for n in range(i):
    if jumpp[n] >= i - n:
      result = 1 + jumpGame(n, jumpp)
      min_Result = min(min_Result, result)

  return min_Result


# Example usage:
jumpp = [2,3,0,1,4]
lastindex = len(jumpp) - 1
print(jumpGame(lastindex, jumpp))  # Output: 3