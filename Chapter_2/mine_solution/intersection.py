from LinkedList import LinkedList

def intersection(ll1, ll2):
    len1 = len(ll1)
    len2 = len(ll2)

    shorter_list = ll1 if len1 < len2 else ll2
    longer_list = ll2 if ll2 > len1 else ll1

    diff = abs(len1 - len2)

    longer_head = longer_list.head
    shorter_head = shorter_list.head

    for i in range(diff):
        longer_head = longer_head.next

    while shorter_head != longer_head:
        shorter_head = shorter_head.next
        longer_head = longer_head.next

    return longer_head
