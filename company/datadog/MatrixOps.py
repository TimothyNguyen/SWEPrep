# Can you write a method that returns the frequency 
# of the max integer in the matrix? In the above example, 
# it would be 1 (since 2 shows up just once).
def maxFromOps(m, n, operations):
    min_col = m
    min_row = n

    for op in operations:
        min_col = min(min_col, op[0])
        min_row = min(min_row, op[1])
    return min_col * min_row

print(maxFromOps(4, 4, [
    [3, 3],
    [2, 1],
]))


