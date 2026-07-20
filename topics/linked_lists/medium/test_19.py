from topics.linked_lists.medium.problem_19 import Solution, ListNode


def list_to_linked(values):
    """Python list -> ListNode chain"""
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_to_list(node):
    """ListNode chain -> Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_remove_from_middle():
    solution = Solution()
    head = list_to_linked([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_to_list(result) == [1, 2, 3, 5]

def test_remove_single_node():
    solution = Solution()
    head = list_to_linked([1])
    result = solution.removeNthFromEnd(head, 1)
    assert result is None

def test_remove_first_of_two():
    solution = Solution()
    head = list_to_linked([1, 2])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_to_list(result) == [2]