
from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    curr = ll.head
    seen_value = set([curr.value])

    while curr.next:
        if curr.next.value in seen_value:
            curr.next = curr.next.next
        else:
            seen_value.add(curr.next.value)
            curr = curr.next
    return ll


def remove_dups_followup(ll):
    if ll.head is None:
        return

    slow_pointer = ll.head
    while slow_pointer:
        fast_pointer = slow_pointer

        while fast_pointer.next:

            if slow_pointer.value == fast_pointer.next.value:
                fast_pointer.next = fast_pointer.next.next
            else:
                fast_pointer = fast_pointer.next

        slow_pointer = slow_pointer.next
    return ll



ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
print('**' * 20 + '\n')
remove_dups(ll)
print(ll)
print('**' * 20 + '\n')
remove_dups_followup(ll)
print(ll)
