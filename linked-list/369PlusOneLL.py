def plusOne(head):
    if not head: return head
    carry = 1
    if head.next is not None: carry = plusOne(head.next, 1)
    if head.val + carry > 9:
        head.val = 0
        return ListNode(1, head)
    head.val += carry
    return head

def plusOne(node, carry):
    if not node.next: carry += plusOne(node.next, carry)
    if node.val + carry > 9:
        node.val = 0
        return 1
    node.val += carry
    return 0
    