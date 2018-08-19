def swap(a, b):
    if not a or not b:
        return
    temp = a.value
    a.value = b.value
    b.value = temp


def sort(head):
    if not head:
        return None
    
    if not head.next:
        return head
    
    node_loop_i = head
    
    while node_loop_i:
        min = node_loop_i.value
        node_loop_j = node_loop_i.next
        swap_node = None
        while node_loop_j:
            if node_loop_j.value < min:
                min = node_loop_j.value
                swap_node = node_loop_j
            node_loop_j = node_loop_j.next
        swap(swap_node, node_loop_i)
        node_loop_i = node_loop_i.next
    
    return head
