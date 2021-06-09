

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_length(head: ListNode) -> int:
    """Get length of LinkedList"""
    count = 0
    while True:
        count += 1
        if head.next is None:
            break
        head = head.next
    return count


def to_list(head: ListNode):
    """convert to python list"""
    values = []
    while True:
        values.append(head.val)
        if head.next is None:
            break
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
    while True:
        binary += str(head.val)
        if head.next is None:
            break
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


def middle_node(head: ListNode):
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
