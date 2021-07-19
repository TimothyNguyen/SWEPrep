class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ans = dict()
        count = 0
        for i in order:
            ans[i] = count
            count += 1
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return False
            
            # Not a valid ordering
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if ans[w1[j]] > ans[w2[j]]:
                        return False
                    break
        return True