class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s=s.replace('()','')
        #     s=s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''
        stack=[]
        closeToopen={")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToopen:
                if stack and stack[-1]==closeToopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False