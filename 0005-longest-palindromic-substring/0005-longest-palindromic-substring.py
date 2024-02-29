class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(stringm,left,right):
            while left>0 and right<len(s)-1 and s[left-1]==s[right+1]:
                left-=1
                right+=1
            return left, right, right-left+1
        
        max_len,left,right=0,0,0
        for ind in range(len(s)-1):
            
            #length of palindrome is odd
            l1, r1, max_len1 = expand(s,ind,ind)
            
            if max_len1>max_len:
                max_len=max_len1
                left,right=l1,r1
            
            #length of palindrome is even
            if s[ind]==s[ind+1]:
                l2,r2,max_len2=expand(s,ind,ind+1)
                
                if max_len2>max_len:
                    max_len=max_len2
                    left,right=l2,r2
        
        return s[left:right+1]
        