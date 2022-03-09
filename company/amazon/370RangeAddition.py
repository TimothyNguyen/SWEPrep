class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        incs = [0] * (length + 1)
        ans = [0] * length
        for i in range(len(updates)):
            incs[updates[i][0]] += updates[i][2]
            incs[updates[i][1] + 1] -= updates[i][2]
            print(incs)
        inc = 0
        for i in range(len(ans)):
            inc += incs[i]
            ans[i] += inc
        return ans