class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if not wordList or endWord not in word_set: return 0
        queue = deque()
        queue.append(beginWord)
        res = 1
        while endWord not in queue:
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                if curr == endWord: return res + 1
                for j in range(len(curr)):
                    word = [x for x in curr]
                    for ch in range(ord('a'), ord('z') + 1):
                        word[j] = chr(ch)
                        charWord = ''.join(word)
                        # print(charWord)
                        if charWord in word_set:
                            word_set.remove(charWord)
                            queue.append(charWord)
            if len(queue) == 0: return 0
            res += 1
        return res
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    - Every adjacent pair of words differs by a single letter.
    - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    - sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
'''