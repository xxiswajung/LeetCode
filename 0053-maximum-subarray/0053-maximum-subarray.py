class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=0
        result_sum=nums[0]
        
        #idea
        #1: 현재 변수가 현재누적합보다 크면, 더 큰 수인 현재 변수로 시작포인트를 갱신해야한다!!
        #2: 음수는 누적합에 도움이 안되기 때문에, 합이 작아지면 갱신해야한다는 것이 포인트
        #3: 현재누적합보다 최종누적합이 더 큰 경우는, 배열을 늘릴수록 maximum에 도움이 안된다는 뜻
        for num in nums:
            max_sum=max(max_sum+num,num) #어디서부터 시작할지 결정하는 변수
            result_sum=max(max_sum, result_sum) #최종적으로 누적된 결과를 저장하는 변수
        return result_sum