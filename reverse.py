def reverse(head):
    if not head:
        return None
    
    if not head.next:
        return head
    
    node = head
    prev = None
    
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev
    
