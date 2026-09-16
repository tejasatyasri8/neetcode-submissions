# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s= "".join(ch.lower() for ch in s if ch.isalnum())
#         i=0
#         j=len(s)-1
#         while(i<j):
#             if(s[i].lower()!=s[j].lower()):
#                 return False
#             i+=1
#             j-=1
#         return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until it hits an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer until it hits an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare lowercase versions
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True