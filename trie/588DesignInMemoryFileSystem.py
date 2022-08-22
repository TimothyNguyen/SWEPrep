from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = defaultdict(TrieNode)
        self.isfile = False

class FileSystem:

    def __init__(self):
        self.top = TrieNode()

    def ls(self, path: str) -> List[str]:
        path_list = path.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children.get(p)
        if node.isfile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans

    def mkdir(self, path: str) -> None:
        path_list = path.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_list = filePath.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children[p]
        node.content += content
        node.isfile = True

    def readContentFromFile(self, filePath: str) -> str:
        path_list = filePath.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children.get(p)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)