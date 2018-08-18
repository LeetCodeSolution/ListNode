from collections import namedtuple

Node = namedtuple('Node', ['value', 'next'])


def create(list):
    if len(list) == 0:
        return None
    
    head = Node(value=list, next=None)
    node = head
    for i in list[1:]:
        next = Node(value=i, next=None)
        node.next = next
        node = next


def output(head):
    node = head
    while node:
        print(node.value)
        node = node.next


list = [4, 1, 5, 8, 3, 7, 4, 6, 2]
head = create(list)
print(head)
