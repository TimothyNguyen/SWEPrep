class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.trie = dict()

        def add_val(num):
            node = self.trie
            str_i = str(num)
            for ch in str_i:
                if ch not in node:
                    node[ch] = dict()
                node = node[ch]
        ans = []
        def dfs(curr_val, curr_node):
            # print(curr_val, curr_node)
            for node in curr_node:
                new_val = curr_val * 10 + int(node)
                ans.append(new_val)
                dfs(new_val, curr_node[node])
        
        for i in range(1, n + 1):
            add_val(i)
        
        for i in range(1, min(10, n+1)):
            ans.append(i)
            child_nodes = self.trie[str(i)]
            dfs(i, child_nodes)

        return ans
        