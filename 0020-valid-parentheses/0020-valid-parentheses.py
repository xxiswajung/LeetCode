class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            item=s[i]
            if item=='(' or item=='[' or item=='{':
                stack.append(item)
            else:
                if stack:
                    if (item==')' and stack[-1]=='(') or (item==']' and stack[-1]=='[') or (item=='}' and stack[-1]=='{'):
                        stack.pop()
                    else:
                        stack.append(item)
                else :
                    stack.append(item)
        
        if stack:
            return False
        else:
            return True