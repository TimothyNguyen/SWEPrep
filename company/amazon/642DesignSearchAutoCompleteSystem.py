class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, sentence:List[chr], freq:int) -> None:
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]          
        node.count += freq

        
    def get_partial_match_sent(self , prefix:str) -> List[str]:
        all_partial_mathes = []
        node = self.root
        prefix_so_far = ""
        for c in prefix:
            if c not in node.children:
                return []
            prefix_so_far += c
            node = node.children[c]
         
       
        def dfs(node, path):
            if node.count > 0: # sentence end
                all_partial_mathes.append((prefix_so_far + ''.join(path[:]), node.count))
            
            for c in node.children:
                path.append(c)
                dfs(node.children[c], path)
                path.pop()
            return
            
        dfs(node, path=[])  # perform dfs to get all sentences that match starting from the end of prefix
        final_res = list(zip(*sorted(all_partial_mathes, key= lambda x: (-x[1],x[0]))[:3]))[0]
        return final_res 



class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.my_trie = Trie()
        self.input_sentence = ''
        
        for sent, time in zip(sentences, times): 
            self.my_trie.insert(sent, time)
            
        
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.my_trie.insert(self.input_sentence, 1)
            self.input_sentence = ''
            return
        
        self.input_sentence += c
        return self.my_trie.get_partial_match_sent(self.input_sentence)
