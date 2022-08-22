import abc 
from abc import ABC, abstractmethod 


class Node(ABC):
    evaluator = {'-':  lambda x,y : x - y,
             '+':  lambda x,y : x + y,
             '/':  lambda x,y : x // y,
             '*':  lambda x,y : x * y
            }
        
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def evaluate(self) -> int:
        if self.val in self.evaluator:
            return self.evaluator[self.val](self.left.evaluate(),self.right.evaluate())
        else:
            return int(self.val) 

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        root = Node(postfix.pop())
        if root.val not in root.evaluator:
            return root
        
        root.right = self.buildTree(postfix)
        root.left = self.buildTree(postfix)
        return root
