
from LinkedList import LinkedList


def delete_middle_node(ll, k):
    # delete the kth stock
    # deleting 3rd stock
    # a b c d e f becomes a b d e f
    before = ll.head
    for i in range(0, k-2, 1):
        before = before.next

    before.next = before.next.next


ll = LinkedList()

ll.generate(10, 0, 99)

print(ll)

delete_middle_node(ll,3)

print(ll)

