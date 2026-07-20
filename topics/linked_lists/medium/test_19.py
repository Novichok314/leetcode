from topics.linked_lists.medium.problem_19 import ListNode, Solution


def test():
    solution = Solution()
    assert solution.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2) == ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
    assert solution.removeNthFromEnd(ListNode(1), 1) == None
    assert solution.removeNthFromEnd(ListNode(1, ListNode(2)), 1) == ListNode(1)
    
