from LinkedList import LinkedList

def sum_lists(ll1,ll2):
	ll3 = LinkedList()

	runner1 = ll1.head
	runner2 = ll2.head


	while runner1 or runner2:
		over = False

		if runner1 is not None and runner2 is not None:
			value = runner1.value + runner2.value
		elif runner1 is None:
			value = runner2.value
		else: value = runner1.value
		

		if value >= 10:
			over = True
			value = value % 10

		ll3.add(value)

		if runner1 is not None:
			runner1 = runner1.next

		if runner2 is not None:
			runner2 = runner2.next

		if over is True:
			if runner1 is not None:
				runner1.value += 1
			elif runner2 is not None:
				runner2.value += 1
			else:
				ll3.add(1)

	return ll3

def sum_list_followup(ll1,ll2):

	len1 = len(ll1)
	len2 = len(ll2)

	if len1 > len2:
		for _ in range(len1 - len2):
			ll2.add_to_beggining(0) 
	else:
		for _ in range(len2 - len1):
			ll1.add_to_beggining(0)

	result=0

	runner1 = ll1.head
	runner2 = ll2.head

	while runner2 and runner1:
		result = result * 10 + runner1.value + runner2.value
		runner2 = runner2.next
		runner1 = runner1.next

	ll3 = LinkedList()
	for num in str(result):
		ll3.add(int(num))

	return ll3





if __name__ == "__main__":
	ll1 = LinkedList()
	ll2 = LinkedList()
	ll1.generate(4,1,9)
	ll2.generate(5,1,9)
	print(ll1)
	print(ll2)
	ll3 = sum_list_followup(ll1,ll2)
	print(ll3)