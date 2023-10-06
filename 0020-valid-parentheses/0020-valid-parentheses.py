class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        s=list(s)
        while s:
            if s[0]=='(' or s[0]=='[' or s[0]=='{':
                stack.append(s.pop(0))
            else:
                if stack and stack[-1]=='(' and s[0]==')':
                    stack.pop()
                    s.pop(0)
                elif stack and stack[-1]=='{' and s[0]=='}':
                    stack.pop()
                    s.pop(0)
                elif stack and stack[-1]=='[' and s[0]==']':
                    stack.pop()
                    s.pop(0)
                else:
                    break
        if len(s)==0 and len(stack)==0:
            return True
        else:
            return False