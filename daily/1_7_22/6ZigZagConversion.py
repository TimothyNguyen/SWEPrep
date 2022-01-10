class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        rowIndex = 0
        goingDown = False
        rows = [''] * numRows
        for ch in s:
            rows[rowIndex] += ch
            if rowIndex == 0 or rowIndex == numRows - 1:
                goingDown = not goingDown
            if goingDown:
                rowIndex += 1
            else:
                rowIndex -= 1
        ans = ''
        for st in rows:
            ans += st
        return ans