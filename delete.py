def delete(head, index):
    if index < 0:
        return head
    
    node = head
    prev = None
    count = 0
    while node:
        if count == index:
            prev.next = node.next
        prev = node
        node = node.next
        count += 1
    
    return head
