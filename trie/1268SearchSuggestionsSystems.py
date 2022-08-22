class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []
        self.size = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
            if node.size < 3:
                node.words.append(word)
                node.size += 1

    def searchPrefix(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return ''
            node = node.children[ch]
        return node.words
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
        ans, curr = [], ''
        for ch in searchWord:
            curr += ch
            ans.append(trie.searchPrefix(curr))
        return ans
        