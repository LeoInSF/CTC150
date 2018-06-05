from LinkedList import LinkedList

def  return_kth_to_last(ll, k):
    runner = curr = ll.head

    if k <= 1:
        return curr

    while k != 1:
        if runner is None:
            return None
        runner = runner.next
        k -= 1

    print runner

    while runner:
        curr = curr.next
        print curr
        runner = runner.next

    return curr


ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
print(return_kth_to_last(ll, 4))
