from base import Node


def append(head, value):
    if not head:
        head = Node(value=value)
        return head
    
    node = head
    
    while node.next:
        node = node.next
    
    node.next = Node(value=value)
    
    return head
