from LinkedList import LinkedList, LinkedListNode

def sum_lists(ll1, ll2):

    head1, head2 = ll1.head, ll2.head
    result = LinkedList()
    carry = 0

    while head1 or head2:
        temp = carry

        if head1:
            temp += head1.value
            head1 = head1.next
        if head2:
            temp += head2.value
            head2 = head2.next

        carry = temp // 10
        left = temp % 10
        node = LinkedListNode(left)
        result.add(node)

    return result

def sum_lists_follow_up(ll1, ll2):
    ## padding with zeros ##
    if (len(ll1) > len(ll2)):
        for i in range(len(ll1) - len(ll2)):
            ll2.add_to_beginning(0)

    if (len(ll2) > len(ll1)):
        for i in range(len(ll2) - len(ll1)):
            ll1.add_to_beginning(0)

    # find sum
    head1, head2 = ll1.head, ll2.head
    result = 0
    while head1 and head2:
        result = result * 10 + head1.value + head2.value
        head1 = head1.next
        head2 = head2.next

    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll

ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(4, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))
print(sum_lists_follow_up(ll_a, ll_b))
