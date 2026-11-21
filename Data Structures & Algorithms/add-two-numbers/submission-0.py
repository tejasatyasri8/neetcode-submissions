# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        str1=""
        str2=""
        temp=l1
        while(temp):
            str1+=str(temp.val)
            temp=temp.next
        temp=l2
        while(temp):
            str2+=str(temp.val)
            temp=temp.next
        str3=str1[::-1]
        str4=str2[::-1]
        str5=str(int(str3)+int(str4))
        str6=str5[::-1]
        dummy=ListNode(-1)
        temp=dummy
        for i in range(len(str6)):
            temp.next=ListNode(int(str6[i]))
            temp=temp.next
        return dummy.next
