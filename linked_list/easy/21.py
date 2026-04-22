class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res = ListNode(0)
        ans = res
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    ans.next = list1
                    list1 = list1.next
                else:
                    ans.next = list2
                    list2 = list2.next
                ans = ans.next
            elif list1:
                ans.next = list1
                break
            elif list2:
                ans.next = list2
                break
        return res.next