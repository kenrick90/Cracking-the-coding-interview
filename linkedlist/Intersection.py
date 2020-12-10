from LinkedList import LinkedList
from LinkedList import LinkedListNode

def intersection(ll1,ll2):

#define a dictionary of value to node
	record = {}

	runner = ll1.head

	while runner:
		record[runner.value] = runner
		runner = runner.next

	runner = ll2.head

	while runner:
		if runner.value in record and record[runner.value] is runner:
			return runner
		runner = runner.next

	return False


if __name__ == '__main__':
	n3 = LinkedListNode(3)
	n2 = LinkedListNode(2,n3)
	n1o1 = LinkedListNode(1,n2)
	n1o2 = LinkedListNode(5,n2)

	ll1 = LinkedList()
	ll1.head = n1o1
	ll1.tail = n3


	ll2 = LinkedList()
	ll2.head = n1o2
	ll2.tail = n3

	print(ll1)
	print(ll2)

	ll3 = LinkedList([1,2,3])
	ll4 = LinkedList([5,2,3])

	print(ll3)
	print(ll4)
	print(intersection(ll1,ll2))