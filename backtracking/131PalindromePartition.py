class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        def isPalindrome(st):
            return st == st[::-1]
        
        def dfs(curr=[], index=1):
            if index == len(s) + 1:
                out.append(list(curr))
                return
            for i in range(index, len(s)+1):
                #print(s[index-1:i])
                if isPalindrome(s[index-1:i]):
                    #print("yes" + s[index-1:i])
                    curr.append(s[index-1:i])
                    dfs(curr, i+1)
                    curr.pop()
        dfs()
        return out