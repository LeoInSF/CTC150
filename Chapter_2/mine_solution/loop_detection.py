from LinkedList import LinkedList


def loop_detection(ll):

    slow = fast = entry = ll.head

    if ll is None or ll.next is None:
        return None

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:

            while(slow is not entry):

                slow = slow.next
                entry = entry.next
            return entry

    return None
