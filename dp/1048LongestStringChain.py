class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {word:None for word in words}

        def dfs(curr):
            if curr not in memo:
                return 0
            result = 0
            if not memo[curr]:
                for i in range(len(curr)):
                    result = max(result, 1 + dfs(curr[:i] + curr[i+1:]))
                    #print(curr + ' ' + str(result))
                memo[curr] = result
            return memo[curr]

        total = 0
        for word in memo:
            total = max(total, dfs(word))
        return total
        '''
          
        words.sort(key=lambda word: len(word))
        d = {word: 1 for word in words}
        answer = 1 # Impossible to have a sequence of length 0.
        
        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in d:
                    d[word] = max(1 + d[prev], d[word])
                    answer = max(answer, d[word])
        
        return answer
        '''