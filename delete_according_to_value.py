def delete_according_to_value(head, value):
    if not head:
        return None
    
    if head.value == value:
        return None
    
    node = head
    prev = None
    while node and node.value != value:
        prev = node
        node = node.next
    
    if not node:
        return head
    
    if node.value == value:
        prev.next = node.next
    
    return head
