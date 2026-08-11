# recurrence: f(i, j) represents jth number in the ith row of the pascal triangle
# recurrence relation: f(i, j) = f(i-1, j-1) + f(i-1, j)
# input i >= 0, 0 <= j <= i
def pascal_triangle(i: int, j: int) -> int:
    if j == 0 or j == i:
        return 1
    else:
        return pascal_triangle(i - 1, j - 1) + pascal_triangle(i - 1, j)


# Return Full triange given the number of rows
def generate_pascals_triangle(num_rows: int) -> list[list[int]]:
    triangle = []
    for i in range(num_rows):
        row = []
        for j in range(i + 1):
            row.append(pascal_triangle(i, j))
        triangle.append(row)
    return triangle

# Example usage:
num_rows = 5    
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)