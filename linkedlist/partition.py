from LinkedList import LinkedList


def partition(ll, x):
    smallerHead = smallerTail = largerHead = largerTail = None
    runner = ll.head
    while runner:
        if runner.value < x:
            if smallerHead is None:
                smallerHead = smallerTail = runner
                runner = runner.next
            else:
                smallerTail.next = runner
                smallerTail = runner
                runner = runner.next
                smallerTail.next = None
        else:
            if largerHead is None:
                largerHead = largerTail = runner
                runner = runner.next
            else:
                largerTail.next = runner
                largerTail = runner
                runner = runner.next
                largerTail.next = None
    if smallerHead is not None:
        smallerTail.next = largerHead
        ll.head = smallerHead
        ll.tail = largerTail



ll = LinkedList()
ll.generate(100, 0, 20)
print(ll)
partition(ll, 1)
print(ll)
