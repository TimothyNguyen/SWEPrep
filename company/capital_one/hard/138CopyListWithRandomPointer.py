'''
A linked list of length n is given such that each node contains 
an additional random pointer, which could point to any node in 
the list, or null.

Construct a deep copy of the list. The deep copy should consist 
of exactly n brand new nodes, where each new node has its 
value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should 
point to new nodes in the copied list such that the pointers 
in the original list and copied list represent the same list 
state. None of the pointers in the new list should point to 
nodes in the original list.

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

HINT: Add a cloned node next to original node
'''

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copy_random_list(head):
        if not head: 
            return head
        
        curr = head
        while curr:
            new_node = Node(curr.val)

            # Insert the cloned node just next to the random node
            next_node = curr.next
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
        
        curr = head
        # Now assign pointers
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # Now remove old nodes
        old_list = head
        new_list = head.next
        head_old = head.next
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        
        return head_old