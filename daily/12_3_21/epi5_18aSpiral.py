'''
: Write a program to enumerate the hrst n pairs of integers (a,b) tn spiral order,
starting from (0,0) followed by (1,0). For example, if n = 10, your output should be
(0, 0), (1,0), (1, -1), (0, -1), (-1, -1), (-1,0), (-1,1), (0, 1), (1, 1), (2,1).
'''
from typing import final


def inverted_spiral(n):
    results = []
    start_col = 0
    end_col = 1
    start_row = 0
    end_row = 1
    final_break = False
    while True:

        # the top row loop
        for i in range(start_col, end_col):
            results.append((start_row, i))
            n -= 1
            if n <= 0:
                final_break = True
                break
        start_col -= 1

        if final_break:
            break

        # the right column
        for i in range(start_row, end_row):
            results.append((i, end_col))
            n -= 1
            if n <= 0:
                final_break = True
                break
        start_row -= 1

        if final_break:
            break

        # bottom row
        for i in range(end_col, start_col, -1):
            results.append((end_row, i))
            n -= 1
            if n <= 0:
                final_break = True
                break
        end_col += 1

        if final_break:
            break

        # the left column
        for i in range(end_row, start_row - 1, -1):
            results.append((i, start_col))
            n -= 1
            if n <= 0:
                final_break = True
                break
        end_row += 1

        if final_break:
            break

    return results