class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for item in tokens:
            if item.isdecimal() or len(item)>1:
                stack.append(int(item))
            else:
                x=stack.pop()
                y=stack.pop()
                if item=='+':
                    stack.append(x+y)
                elif item=='-':
                    stack.append(y-x)
                elif item=='*':
                    stack.append(x*y)
                else:
                    result=y/x
                    stack.append(int(result))
        return stack[0]