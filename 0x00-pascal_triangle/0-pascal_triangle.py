def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows
    """
    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:
            last_row = triangle[-1]
            # Calculate each element of the current row based on the previous row
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Test the function with an example
print_triangle(pascal_triangle(5))

