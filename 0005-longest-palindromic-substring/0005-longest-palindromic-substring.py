class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        start,end=0,1 #나중에 결과 출력할 때, 어디서부터 어디까지 출력할지 표시할 index
        
        #base cases
        #문자열의 길이가 1인 경우 무조건 True
        for i in range(n):
            dp[i][i]=True
            #문자열의 길이가 2인데, 두 글자 모두 같으면 True
            #i<n-1가 있는 이유 : s[i+1] 의 범위도 생각해야하기 때문
            if i<n-1 and s[i]==s[i+1]:
                dp[i][i+1]=True
                start=i
                end=2

        #reputation
        #문자열의 길이가 3 이상인 경우
        for length in range(3,n+1):
            for i in range(n-length+1):
                j=i+length-1
                dp[i][j]=(s[i]==s[j]) and dp[i+1][j-1]
                #가장 긴 문자열의 정보 갱신
                if dp[i][j] and length>end:
                    start=i
                    end=length
                    
        return s[start:start+end]