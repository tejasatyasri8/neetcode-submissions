# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        arr1=[]
        temp=head
        while(temp):
            arr1.append(temp)
            temp=temp.next
        arr1.pop(len(arr1)-n)
        if len(arr1) == 0:
            return None
        for i in range(len(arr1)-1):
            arr1[i].next=arr1[i+1]
        arr1[-1].next=None
        return arr1[0]