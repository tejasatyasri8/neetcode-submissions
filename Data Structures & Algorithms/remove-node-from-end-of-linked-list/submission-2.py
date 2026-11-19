# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # arr1=[]
        # temp=head
        # while(temp):
        #     arr1.append(temp)
        #     temp=temp.next
        # arr1.pop(len(arr1)-n)
        # if len(arr1) == 0:
        #     return None
        # for i in range(len(arr1)-1):
        #     arr1[i].next=arr1[i+1]
        # arr1[-1].next=None
        # return arr1[0]
        length=0
        temp=head
        while(temp):
            length+=1
            temp=temp.next
        removable_index=length-n
        print(length)
        print(removable_index)
        if(length==0 or length==1):
            return None
        if(removable_index==0):
            return head.next
        temp=head
        count=0
        while(temp):
            if(count==removable_index-1):
                print(count)
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1
        return head
        
