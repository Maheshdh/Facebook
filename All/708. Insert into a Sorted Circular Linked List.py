"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        if head.next == None:
            if head.val > insertVal:
                new_node.next = head
                head.next = new_node
                head = new_node
                return head
        else:
            cur_node = head
            next_node = head.next
            while next_node != head:
                if new_node.val <= next_node.val and new_node.val >= cur_node.val:
                    cur_node.next = new_node
                    new_node.next = next_node
                    return head
                elif(cur_node.val > next_node.val):
                    if(insertVal >= cur_node.val or insertVal <= next_node.val):
                        cur_node.next = new_node
                        new_node.next = next_node
                        return head
                cur_node = next_node
                next_node = next_node.next

            cur_node.next = new_node
            new_node.next = head
            return head



        
