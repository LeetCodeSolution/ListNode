from base import Node
from create import create
from output import output
from reverse_output import reverse_output, reverse_output_recursively
from reverse import reverse
from delete import delete
from append import append
from delete_according_to_value import delete_according_to_value
from insert import insert
from sort import sort

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

append(head, 40)
output(head)

delete_according_to_value(head, 40)
output(head)

delete_according_to_value(head, 8)
output(head)

head = insert(head, 0, 33)
output(head)

sort(head)
output(head)
