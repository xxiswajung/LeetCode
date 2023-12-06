class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone=[0]*10
        phone[2]=['a','b','c']
        phone[3]=['d','e','f']
        phone[4]=['g','h','i']
        phone[5]=['j','k','l']
        phone[6]=['m','n','o']
        phone[7]=['p','q','r','s']
        phone[8]=['t','u','v']
        phone[9]=['w','x','y','z']
        
        global ans
        ans=''
        res=[]
        
        def DFS(v):
            global ans
            if v==len(digits):
                res.append(ans)
                return
            else:
                for x in phone[int(digits[v])]:
                    ans+=x
                    DFS(v+1)
                    ans=ans[:-1]
        
        if digits=="":
            return []
        else:
            DFS(0)
            return res