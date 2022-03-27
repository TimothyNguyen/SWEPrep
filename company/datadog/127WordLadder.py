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
      