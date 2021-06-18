
from typing import List
from random import randint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def to_str(head: ListNode) -> str:
    return ' -> '.join([str(x) for x in to_list(head)])


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


def concatenate(l1: ListNode, l2: ListNode):
    """concatenate two lists"""
    while l1.next:
        l1 = l1.next
    l1.next = l2


def reverse_list(head: ListNode) -> ListNode:
    """
    LeetCode 206

    Given the head of a singly linked list,
    reverse the list, and return the reversed list.
    """
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        new = reverse_list(head.next)
        concatenate(new, head)
        head.next = None
        return new


def reverse_list_iterative(head: ListNode) -> ListNode:
    """
    LeetCode 206 - Best Practice
    """
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def is_palindrome(head: ListNode) -> bool:
    """
    LeetCode 234

    Given the head of a singly linked list,
    return true if it is a palindrome.
    """
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values == values[::-1]


def is_palindrome_bp(head: ListNode) -> bool:
    """
    LeetCode 234 - best practice
    O(N) time complexity, O(N/2) space complexity

    Three steps:
    1. Find the midpoint of the linked list
    2. Push the second half values into the stack
    3. Pop values out from stack, and compare the to the first half of the linked list

    """

    if not head or not head.next:
        return True

    slow = fast = cur = head

    # 1. Get the midpoint (slow)
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Compare
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    """
    LeetCode 160

    Given the heads of two singly linked-lists headA and headB,
    return the node at which the two lists intersect.
    If the two linked lists have no intersection at all, return null.
    """

    # Dummy solution - Time Limit Exceeded

    # while head_a:
    #     copy_b = head_b
    #     while copy_b:
    #         if copy_b == head_a:
    #             return head_a
    #         copy_b = copy_b.next
    #     head_a = head_a.next
    # return None

    len_a = get_length(head_a)
    len_b = get_length(head_b)

    if len_a > len_b:
        for _ in range(len_a - len_b):
            head_a = head_a.next

    if len_b > len_a:
        for _ in range(len_b - len_a):
            head_b = head_b.next

    while head_a and head_b:

        if head_a == head_b:
            return head_a

        head_a = head_a.next
        head_b = head_b.next

    return None


def get_intersection_node_bp(head_a: ListNode, head_b: ListNode) -> ListNode:
    """
    LeetCode 160 - best practice
    """
    a, b = head_a, head_b
    while a != b:
        a = a.next if a else head_a
        b = b.next if b else head_b
    return a
    # only 2 ways to get out of the loop,
    # they meet or the both hit the end=None


def has_cycle(head: ListNode) -> bool:
    """
    LeetCode - 141

    Given head, the head of a linked list,
    determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node
    in the list that can be reached again by continuously
    following the next pointer. Internally, pos is used to
    denote the index of the node that tail's next pointer
    is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.
    """
    occurrence = set()
    while head:
        if head in occurrence:
            return True
        else:
            occurrence.add(head)
        head = head.next
    return False


def has_cycle_bp(head: ListNode) -> bool:
    """
    Tortoise and hare approach - best practice

    Uses O(1) memory

    https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
    """
    try:
        slow = head
        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


def delete_duplicates(head: ListNode) -> ListNode:
    """
    LeetCode - 83

    Given the head of a sorted linked list, delete all duplicates
    such that each element appears only once. Return the linked list sorted as well.
    """
    copy = head
    while copy and copy.next:
        if copy.val == copy.next.val:
            delete_node(copy)              # remove first duplicate (among 2)
            # copy.next = copy.next.next   # remove second duplicate (among 2) - BP
        else:
            copy = copy.next
    return head


def append(list1: ListNode, list2: ListNode):
    """Append list2 to the end of list1"""
    while list1.next:
        list1 = list1.next
    list1.next = list2


def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    """
    LeetCode - 1669
    """
    copy = list1
    index = 0
    start, end = None, None

    while copy:
        if index == a - 1:
            start = copy
        elif index == b:
            end = copy
            break
        copy = copy.next
        index += 1

    append(list2, end.next)
    start.next = list2
    return list1


def swap_nodes(head: ListNode, k: int) -> ListNode:
    """
    LeetCode - 1721

    You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the
    kth node from the beginning and the kth node from the end (the list is 1-indexed).
    """
    length = get_length(head)
    copy = head
    first, second = None, None

    for i in range(1, length + 1):
        if i == k:
            first = copy
        if i == length + 1 - k:
            second = copy
        copy = copy.next

    first.val, second.val = second.val, first.val
    return head


def swap_nodes_bp(head: ListNode, k: int) -> ListNode:
    """
    LeetCode - 1721

    Leveraging a moving window of size len(head) - k
    """
    n1, n2, p = None, None, head
    while p is not None:

        k -= 1
        n2 = None if n2 is None else n2.next
        if k == 0:
            # start iterating n2 only when k-th node is reached
            n1 = p
            n2 = head
        p = p.next

    n1.val, n2.val = n2.val, n1.val
    return head


def get_random(head: ListNode) -> int:
    """
    LeetCode - 382

    Given a singly linked list,
    return a random node's value from the linked list.
    Each node must have the same probability of being chosen.

    Good solution when list has static size
    """
    length = get_length(head)
    index = randint(0, length - 1)
    copy = head
    counter = 0

    while copy:
        if counter == index:
            return copy.val
        copy = copy.next
        counter += 1


def get_random_bp(head: ListNode) -> int:
    """
    LeetCode - 382

    Reservoir Sampling approach - for infinite sequences or dynamically changing sizes
    """
    result, node, index = head, head.next, 1

    while node:
        if randint(0, index) is 0:
            result = node
        node = node.next
        index += 1
    return result.val


def num_components(head: ListNode, nums: List[int]) -> int:
    """
    LeetCode - 817
    """
    counter = 0
    in_component = False

    while head:
        if head.val in nums:
            if not in_component:
                in_component = True
        else:
            if in_component:
                counter += 1
                in_component = False
        head = head.next

    if in_component:
        counter += 1

    return counter


def odd_even_list(head: ListNode) -> ListNode:
    """
    LeetCode - 328

    Given the head of a singly linked list, group all the nodes with odd
    indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.
    """
    odd = None
    even = None
    counter = 1

    while head:

        if counter % 2 == 1:
            if odd is None:
                odd_iter = ListNode(head.val)
                odd = odd_iter
            else:
                odd_iter.next = ListNode(head.val)
                odd_iter = odd_iter.next

        else:
            if even is None:
                even_iter = ListNode(head.val)
                even = even_iter
            else:
                even_iter.next = ListNode(head.val)
                even_iter = even_iter.next

        counter += 1
        head = head.next

    if odd is None:
        return even
    if even is None:
        return odd

    append(odd, even)
    return odd


def odd_even_list_bp(head: ListNode) -> ListNode:
    """
    LeetCode - 328
    Satisfies O(1) space complexity condition
    """
    if head:
        odd = head
        even = head.next
        eHead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = eHead
    return head
