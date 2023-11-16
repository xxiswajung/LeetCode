class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 문자열의 처음부터 i까지의 부분 문자열이 나눌수 있는지의 여부 확인
        dp=[False]*(len(s)+1)
        dp[0]=True
        
        # 문자열 순회
        for i in range(1, len(s)+1):
            # 이전까지의 부분 문자열이 나눌 수 있는지 여부 확인
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True 
                    break
        return dp[len(s)]