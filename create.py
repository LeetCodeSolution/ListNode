from base import Node


def create(list):
    if len(list) == 0:
        return None
    
    head = Node(value=list[0])
    node = head
    for i in list[1:]:
        next = Node(value=i)
        node.next = next
        node = next
    return head
