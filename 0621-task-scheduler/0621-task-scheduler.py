class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts=Counter(tasks).values()
        M=max(task_counts)
        Mct = sum(1 for count in task_counts if count==M)
        return max(len(tasks),(n+1)*(M-1)+Mct)
        
        # task_counts = Counter(tasks).values()
        # M = max(task_counts) # 최대 빈도를 가진 작업의 빈도수 
        # Mct = sum(1 for count in task_counts if count == M) # 최대 빈도를 가진 작업의 개수 
        # return max(len(tasks), (M - 1) * (n + 1) + Mct) 
        # # (M-1)*(n+1) : 반복되는 chunk의 길이를 계산, A _ _ A _ _ 이럴때, A _ _ 의 길이를 구하고, (A개수-1) 만큼 곱하기
        # # Mct를 나중에 더하는 이유 : 결국 마지막에 가장 빈도수가 높은 것들이 마지막에 남기 때문 