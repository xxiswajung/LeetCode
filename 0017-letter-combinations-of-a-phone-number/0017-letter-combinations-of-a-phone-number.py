class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        tmp=''
        answer=[]
        
        if len(digits)==0:
            return answer
        
        def DFS(v):
            nonlocal tmp, answer
            if v==len(digits):
                answer.append(tmp)
                return
            else:
                item=digits[v]
                for i in range(len(phone[item])):
                    tmp+=phone[item][i]
                    DFS(v+1)
                    tmp=tmp[:len(tmp)-1]
        DFS(0)
        return answer
            