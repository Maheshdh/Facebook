class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.add(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]
    
    def add(self, node):
        last_node = self.tail.prev
        last_node.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = last_node
    
    def remove(self,node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
