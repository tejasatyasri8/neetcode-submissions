# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list1=[]
        for i in range(len(lists)):
            temp=lists[i]
            while(temp):
                list1.append(temp.val)
                temp=temp.next
        list1.sort()
        dummy=ListNode(-1)
        temp=dummy
        for i in range(len(list1)):
            temp.next=ListNode(list1[i])
            temp=temp.next
        return dummy.next