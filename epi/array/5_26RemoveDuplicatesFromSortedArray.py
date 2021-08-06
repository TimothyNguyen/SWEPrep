class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        if not A: return 0
        write_index = 1
        for i in range(1, len(A)):
            if A[write_index - 1] != A[i]:
                A[write_index] = A[i]
                write_index += 1
        return write_index