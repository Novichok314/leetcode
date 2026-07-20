"""
LeetCode 21
Topic: linked_lists
Difficulty: easy
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None and list2 is None: 
            return None 
        if list1 is None: 
            return list2
        if list2 is None: 
            return list1 

        head = ListNode(None) 
        head_iter = head
        while list1 and list2: 
            if list1.val < list2.val: 
                head_iter.next = list1 
                list1 = list1.next 
            else:
                head_iter.next = list2 
                list2 = list2.next
            head_iter = head_iter.next
        if list1:
            head_iter.next = list1
        if list2:
            head_iter.next = list2
        return head.next

        


if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeTwoLists())
