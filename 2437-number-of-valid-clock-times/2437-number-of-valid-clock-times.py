class Solution:
    def countTime(self, time: str) -> int:
        answer=1
        for i in range(len(time)):
            if time[i]=='?':
                if i==0:
                    if time[1]=='?':
                        continue
                    if 4<=int(time[1])<=9:
                        answer*=2
                    elif 0<=int(time[1])<=3:
                        answer*=3
                elif i==1:
                    if time[0]=='0' or time[0]=='1':
                        answer*=10
                    elif time[0]=='2':
                        answer*=4
                    else:
                        answer*=24
                elif i==3:
                    answer*=6
                elif i==4:
                    answer*=10
        return answer