def output(head):
    print('Output')
    node = head
    while node:
        print(node.value, end=' ')
        node = node.next
    print()
