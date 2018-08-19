from base import Node


def insert(head, index, value):
    if index < 0:
        return head
    
    if not head and index > 0:
        return head
    
    if index == 0:
        new = Node(value=value)
        new.next = head
        head = new
        return head
    
    node = head
    prev = None
    step = 0
    
    while node and step < index:
        prev = node
        node = node.next
        step += 1
    
    if not node:
        return head
    
    next = prev.next
    new = Node(value=value)
    prev.next = new
    new.next = next
    
    return head
