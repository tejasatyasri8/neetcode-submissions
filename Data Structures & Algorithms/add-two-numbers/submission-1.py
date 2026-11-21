# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # str1=""
        # str2=""
        # temp=l1
        # while(temp):
        #     str1+=str(temp.val)
        #     temp=temp.next
        # temp=l2
        # while(temp):
        #     str2+=str(temp.val)
        #     temp=temp.next
        # str3=str(int(str1)+int(str2))
        # dummy=ListNode(-1)
        # temp=dummy
        # for i in range(len(str3)):
        #     temp.next=ListNode(int(str3[i]))
        #     temp=temp.next
        # return dummy.next
        dummy=ListNode(-1)
        curr=dummy
        carry=0
        t1=l1
        t2=l2
        while(t1 or t2):
            sum1=carry
            if t1:
                sum1+=t1.val
                t1=t1.next
            if t2:
                sum1+=t2.val
                t2=t2.next
            curr.next=ListNode(int(sum1%10))
            carry=int(sum1/10)
            curr=curr.next
        if carry:
            curr.next=ListNode(carry)
        return dummy.next





