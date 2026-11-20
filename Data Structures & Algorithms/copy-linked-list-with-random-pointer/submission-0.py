"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import deque
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp=head
        dict1={}
        while(temp):
            dict1[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        head1=dict1[temp]
        while(temp):
            if temp.next is not None:
                dict1[temp].next=dict1[temp.next]
            else:
                dict1[temp].next=None

            if temp.random is not None:
                dict1[temp].random=dict1[temp.random]
            else:
                dict1[temp].random=None
            temp=temp.next
        return head1
            
        



        