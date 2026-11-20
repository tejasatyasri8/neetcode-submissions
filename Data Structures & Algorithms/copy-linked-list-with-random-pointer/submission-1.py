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
        # temp=head
        # dict1={}
        # while(temp):
        #     dict1[temp]=Node(temp.val)
        #     temp=temp.next
        # temp=head
        # head1=dict1[temp]
        # while(temp):
        #     if temp.next is not None:
        #         dict1[temp].next=dict1[temp.next]
        #     else:
        #         dict1[temp].next=None

        #     if temp.random is not None:
        #         dict1[temp].random=dict1[temp.random]
        #     else:
        #         dict1[temp].random=None
        #     temp=temp.next
        # return head1
        temp=head
        while(temp):
            x=temp.val
            new_node=Node(x)
            new_node.next=temp.next
            temp.next=new_node
            temp=temp.next.next
        temp=head
        while(temp):
            if(temp.random):
                temp.next.random=temp.random.next
            else:
                temp.next.random=None
            temp=temp.next.next
        temp=head
        dummy=Node(-1)
        res=dummy
        while(temp):
            res.next=temp.next
            temp.next=res.next.next
            temp=temp.next
            res=res.next
        return dummy.next









