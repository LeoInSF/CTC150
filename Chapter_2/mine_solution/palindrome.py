from LinkedList import LinkedList

# def is_palindrome(ll):
#     if ll.head and ll.head.next is None:
#         return True
#
#     if ll.head and ll.head.next and ll.head.value == ll.head.next.value:
#         return True
#
#     slow = fast = ll.head
#
#     while fast.next:
#         fast = fast.next
#     if slow.value == fast.value:
#         ll.head = ll.head.next
#         ll.tail = fast
#         print ll
#         return (is_palindrome(ll))
#
#     return False


def is_palindrome(ll):
    slow = fast = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False
        slow = slow.next

    return True

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([4, 3, 2, 1])
print(ll)
print(is_palindrome(ll))








'''
Hints
1) original linked list == reversed linked list
2) try using stack
3) if you have the length of the linked list, could you do it recursively?
4)
'''
