# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        values=[]
        while curr:
            values.append(curr)
            curr=curr.next
        i=0
        j=len(values)-1
        curr=head
        while(i<j):
            curr.next=values[j]
            curr=curr.next
            j-=1
            curr.next=values[i+1]
            curr=curr.next
            i+=1
        curr.next=None
            
