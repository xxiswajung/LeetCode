class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        while tokens:
            item=tokens.pop(0)
            if item.isdecimal() or (item[0]=='-' and len(item)>1):
                stack.append(int(item))
            else:
                val1=stack.pop()
                val2=stack.pop()
                if item=='+':
                    stack.append(val1+val2)
                elif item=='-':
                    stack.append(val2-val1)
                elif item=='*':
                    stack.append(val1*val2)
                else:
                    stack.append(int(val2/val1))
        return stack[0]