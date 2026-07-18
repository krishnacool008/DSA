def TestFunc(x):
    # Example implementation; replace with actual logic that might throw an exception
    if x <= 0:  # Simulate failure for a specific value, e.g., 'b'
        raise ValueError("Function failed for input:", x)
    return f"Function succeeded for input {x}"

# Variables to test
variables = [-11, -1, 4, -2, -3, 4]

# Test each variable and catch exceptions
for var in variables:
    try:
        result = TestFunc(var)
        print(result)
        break
    except Exception as e:
        print(f"TestFunc failed for variable '{var}' with error: {e}")




    