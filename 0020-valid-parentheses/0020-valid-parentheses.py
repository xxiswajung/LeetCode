class Solution:
    def isValid(self, s: str) -> bool:
#         stack=[]
#         for i in range(len(s)):
#             item=s[i]
#             if item=='(' or item=='[' or item=='{':
#                 stack.append(item)
#             else:
#                 if stack:
#                     if (item==')' and stack[-1]=='(') or (item==']' and stack[-1]=='[') or (item=='}' and stack[-1]=='{'):
#                         stack.pop()
#                     else:
#                         stack.append(item)
#                 else :
#                     stack.append(item)
        
#         if stack:
#             return False
#         else:
#             return True
        
        
        
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        
        for char in s:
            if stack and char in mapping:
                item=stack.pop()
                if mapping[char]!=item:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True