class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        op=''.join(list(p)[::-1])
        dict1=defaultdict(int)
        for x in op:
            dict1[x]+=1
        ans=[]
        
        for i in range(len(s)):
            for x in dict1:
                if s[i:i+len(op)].count(x)!=dict1[x]:
                    break
            else:
                ans.append(i)
        return ans