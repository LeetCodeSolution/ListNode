def reverse_output(head):
    values = []
    node = head
    
    while node:
        values.append(node.value)
        node = node.next
    
    for _ in range(len(values)):
        print(values.pop(), end=' ')
    
    print()


def reverse_output_recursively(head):
    node = head
    
    if node:
        reverse_output_recursively(node.next)
        print(node.value, end=' ')
