def inverted_spiral(n):
    results = []
    for i in range(n):
        results.push([])
    
    counter = 1
    start_col = 0
    end_col = n - 1
    start_row = 0
    end_row = n - 1

    while start_col <= end_col and start_row <= end_row:
        # the top row loop
        for i in range(start_col, end_col + 1):
            results[start_row][i] = counter
            counter += 1
        start_row += 1
    
        # right column
        for i in range(start_row, end_row + 1):
            results[i][end_col] = counter
            counter += 1
        end_col -= 1

        # bottom row
        for i in range(end_col, start_col - 1, -1):
            results[end_row][i] = counter
            counter += 1
        end_row -= 1

        # left column
        for i in range(end_row, start_row - 1, -1):
            results[i][start_col] = counter
            counter += 1
        start_col += 1
    return results