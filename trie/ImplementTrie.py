class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string):
        node = self.root
        for ch in string:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True
    
    def search(self, string):
        node = self.root
        for ch in string:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word
    
    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
