from base import Node
from output import output
from reverse_output import reverse_output, reverse_output_recursively
from reverse import reverse
from delete import delete


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


list = [4, 1, 5, 8, 3, 7, 4, 6, 2]
head = create(list)
print(head)
output(head)
reverse_output(head)
reverse_output_recursively(head)

head = reverse(head)
print()
output(head)

delete(head, 2)
output(head)
