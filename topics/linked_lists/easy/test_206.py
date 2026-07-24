from topics.linked_lists.easy.problem_206 import ListNode, Solution


def test():
    solution = Solution()
    res = solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    for i in range(5, 0, -1):
        assert i == res.val
        res = res.next
