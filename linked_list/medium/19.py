class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next: return None
        dummy_node =  ListNode(0)
        dummy_node.next = head
        slw_ptr = dummy_node
        fst_ptr = dummy_node
        diff = 0
        while fst_ptr:
            if diff == n + 1:
                slw_ptr = slw_ptr.next
                diff -= 1
            fst_ptr = fst_ptr.next
            diff += 1
        slw_ptr.next = slw_ptr.next.next
        return dummy_node.next