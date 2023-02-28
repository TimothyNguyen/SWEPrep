'''
There is a new alien language that uses the English alphabet. However, the order 
among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the 
strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically 
increasing order by the new language's rules. If there is no solution, return "". If there 
are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they 
differ, the letter in s comes before the letter in t in the alien language. If the first 
min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        if len(words) == 0:
            return ""

        graph = dict()
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = []
        
        # Step 1: Find all edges and put them in reverse_adj_list.
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            j = 0
            while j < min_len:
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
                j += 1

        visited_letters = dict()
        ans = []
        print(graph)

        def dfs(c):
            if c in visited_letters:
                return visited_letters[c]
            visited_letters[c] = True
            for nei in graph[c]:
                if dfs(nei):
                    return True
            visited_letters[c] = False
            ans.append(c)
            return False

        for ch in graph:
            if dfs(ch):
                return ""
        return "".join(reversed(ans))