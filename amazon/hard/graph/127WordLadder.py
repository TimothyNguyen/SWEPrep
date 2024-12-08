class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        num_words = 0
        if endWord not in word_set:
            return num_words
        queue = deque()
        queue.append(beginWord)
        while queue:
            l = len(queue)
            for i in range(l):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return num_words + 1
                new_word_arr = [x for x in curr_word]
                for ch_idx in range(len(curr_word)):
                    for ch in range(ord('a'), ord('z') + 1):
                        new_word_arr[ch_idx] = chr(ch)
                        new_word = ''.join(new_word_arr)
                        if new_word in word_set:
                            queue.append(new_word)
                            word_set.remove(new_word)
                    new_word_arr[ch_idx] = curr_word[ch_idx]
            num_words += 1
        return 0