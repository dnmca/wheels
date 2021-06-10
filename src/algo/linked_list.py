

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_length(head: ListNode) -> int:
    """Get length of LinkedList"""
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def to_list(head: ListNode) -> list:
    """convert to python list"""

    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def get_decimal_value(head: ListNode) -> int:
    """
    LeetCode 1290

    Given head which is a reference node to a singly-linked list.
    The value of each node in the linked list is either 0 or 1.
    The linked list holds the binary representation of a number.

    Return the decimal value of the number in the linked list.
    """
    binary = ''
    while head:
        binary += str(head.val)
        head = head.next
    return int(binary, 2)


def delete_node(node: ListNode):
    """
    LeetCode 237

    Write a function to delete a node in a singly-linked list.
    You will not be given access to the head of the list,
    instead you will be given access to the node to be deleted directly.

    It is guaranteed that the node to be deleted is not a tail node in the list.
    """
    node.val = node.next.val
    node.next = node.next.next


def middle_node(head: ListNode) -> ListNode:
    """
    LeetCode 876

    Given a non-empty, singly linked list with head node head,
    return a middle node of linked list.

    If there are two middle nodes, return the second middle node.
    """
    mid = get_length(head) // 2
    idx = 0
    while True:
        if idx == mid:
            return head.val
        head = head.next
        idx += 1


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    LeetCode 21

    Merge two sorted linked lists and return it as a sorted list.
    The list should be made by splicing together the nodes of the first two lists.
    """

    head = None

    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                value = l1.val
                l1 = l1.next
            else:
                value = l2.val
                l2 = l2.next
        elif l1:
            value = l1.val
            l1 = l1.next
        elif l2:
            value = l2.val
            l2 = l2.next

        if head is None:
            head = ListNode(value)
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(value)
    return head


def merge_two_lists_recursive(l1: ListNode, l2: ListNode) -> ListNode:
    """
    LeetCode 21 - Best Practice
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursive(l1, l2.next)
        return l2


def remove_elements(head: ListNode, val: int) -> ListNode:
    """
    LeetCode 203

    Given the head of a linked list and an integer val,
    remove all the nodes of the linked list that has
    Node.val == val, and return the new head.
    """

    # it is possible to solve this problem with iteration
    # (add dummy node in front and return dummy.next at the end)

    if head is None:
        return None
    elif head.val == val:
        return remove_elements(head.next, val)
    else:
        head.next = remove_elements(head.next, val)
        return head
