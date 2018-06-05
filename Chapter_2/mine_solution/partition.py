from LinkedList import LinkedList, LinkedListNode

def partition(ll, x):

    head1 = LinkedListNode(0)
    head2 = LinkedListNode(0)

    temp = ll.head
    phead1 = head1
    phead2 = head2

    while temp:

        if temp.value < x:
            phead1.next = temp
            temp = temp.next
            phead1 = phead1.next
            phead1.next = None
        else:
            phead2.next = temp
            temp = temp.next
            phead2 = phead2.next
            phead2.next = None

    phead1.next = head2.next
    head = head1.next
    return head


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
new_head = partition(ll, ll.head.value)
print(ll)
while new_head:
    print(new_head)
    new_head = new_head.next
