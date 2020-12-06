from LinkedList import LinkedList


def partition(ll, x):
    runner = ll.head
    left = right = None
    while runner.next:
        if runner.value < x:
            if left is None:
                ll.head = left = runner
            else:
                left.next = runner
                if left.next:
                    left = left.next

        if runner.value >= x:
            if right is None:
                right = righthead = runner
            else:
                right.next = runner
                right = right.next

        runner = runner.next

    left.next = righthead



ll = LinkedList()
ll.generate(10, 0, 20)
print(ll)
partition(ll, 5)
print(ll)
