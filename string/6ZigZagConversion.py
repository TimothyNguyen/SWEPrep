class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1: return s
        rowIndex = 0
        goingDown = False
        rows = ['']*numRows
        for x in s:
            rows[rowIndex] += x
            if rowIndex == 0 or rowIndex == numRows - 1:
                goingDown = not goingDown
            rowIndex = rowIndex + 1 if goingDown else rowIndex - 1
            # print(rowIndex)
        return ''.join(rows)