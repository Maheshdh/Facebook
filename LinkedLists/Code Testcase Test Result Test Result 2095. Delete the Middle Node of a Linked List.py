# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self,head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        middleNode = self.findMiddle(head)
        if middleNode == head:
            return None
        cur_node, previous_node = head, None
        while cur_node != middleNode:
            previous_node = cur_node
            cur_node = cur_node.next
        previous_node.next = cur_node.next
        cur_node.next = None
        return head
