from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict(TrieNode)  # Easy to insert new node.
        self.words = list()
        self.size = 0  # True for the end of the trie.


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            curr = curr.children[char]
            if curr.size < 3:
                curr.words.append(word)
                curr.size += 1

    def findWordByPrefix(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return ''
            curr = curr.children[c]
        return curr.words
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products: trie.insert(word)
        ans, curr = [], ''
        for c in searchWord:
            curr += c
            ans.append(trie.findWordByPrefix(curr))
        return ans