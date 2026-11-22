class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    def insert(self,node:node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next=node
        node.next.prev=node
    def remove(self,node:Node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        temp=Node(key,value)
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache)>=self.capacity:
            lru=self.tail.prev
            self.remove(lru)
            self.cache.pop(lru.key)
        self.cache[key]=temp
        self.insert(self.cache[key])
        


        
