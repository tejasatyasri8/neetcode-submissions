# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # list1=[]
        # for i in range(len(lists)):
        #     temp=lists[i]
        #     while(temp):
        #         list1.append(temp.val)
        #         temp=temp.next
        # list1.sort()
        # dummy=ListNode(-1)
        # temp=dummy
        # for i in range(len(list1)):
        #     temp.next=ListNode(list1[i])
        #     temp=temp.next
        # return dummy.next
    #     if not lists:
    #         return None
    #     result=lists[0]
        
    #     for i in range(1,len(lists)):
    #         result=self.merge2lists(result,lists[i])
    #     return result
    # def merge2lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     temp1=list1
    #     temp2=list2
    #     dummy = ListNode(-1)
    #     prev = dummy

    #     while(temp1 and temp2):
    #         if(temp1.val>=temp2.val):
    #             prev.next=temp2
    #             temp2=temp2.next
    #         else:
    #             prev.next=temp1
    #             temp1=temp1.next
    #         prev=prev.next
    #     if temp1:
    #         prev.next=temp1
    #     else:
    #         prev.next=temp2
    #     return dummy.next
        pq=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))
        dummy=ListNode(-1)
        temp=dummy
        while(pq):
            x,i,y = heapq.heappop(pq)
            temp.next=y
            if y.next:
                heapq.heappush(pq,(y.next.val,i,y.next))
            temp=temp.next
        return dummy.next



            

















