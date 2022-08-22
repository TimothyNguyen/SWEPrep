'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
'''
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # algorithm: dp+Trie
        # step1: for each word, run dp 
        # dp[n] = any(dp[i] and dp[j] for i: 0~n and j: i~n)
        # time-complexity: O(N1*L^2)
        # space-complexity: O(N2) N2 is the sum(words[i].length)

        def search(start, end):
            cur = dummy
            for i in range(start, end):
                if w[i] not in cur.children:
                    return
                cur = cur.children[w[i]]
                if start == 0 and i == end - 1:
                    return
                if cur.end:
                    dp[i] = cur.end

        cur = dummy = TrieNode()
        for w in words:
            cur = dummy
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.end = True
        
        res = []
        for w in words:
            size = len(w)
            dp = [False] * size
            dp.append(True)
            for i in range(-1, size):
                if not dp[i]:
                    continue
                search(i+1, size)
            if size and dp[-2]:
                res.append(w)
        return res


