class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def canForm(word, trie, memo):
            if word in memo:
                return memo[word]
            
            node = trie.root
            for i in range(len(word)):
                if word[i] in node.children:
                    node = node.children[word[i]]
                    if node.is_word:
                        remaining_word = word[i + 1:]
                        if remaining_word and (trie.search(remaining_word) or canForm(remaining_word, trie, memo)):
                            memo[word] = True
                            return True
                else:
                    break
            memo[word] = False
            return False
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        memo = {}
        concatenated_words = []
        # Check each word if it can be formed by concatenating other words
        for word in words:
            if canForm(word, trie, memo):
                concatenated_words.append(word)
        return concatenated_words