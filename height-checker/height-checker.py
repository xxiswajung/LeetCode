class Solution(object):
    def heightChecker(self, heights):
        expected = heights[:]
        
        while True:
            flag = 1
            i = 0 
            j = 1
            for i in range(len(heights)-1):
                if expected[i]>expected[j]:
                    expected[i], expected[j] = expected[j], expected[i]
                    flag = 0
                j+=1
            if flag == 1:
                break
        cnt = 0
        for k in range(len(heights)):
            if heights[k]!=expected[k]:
                cnt+=1
        return cnt
                
        