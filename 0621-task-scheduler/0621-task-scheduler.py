class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        M = max(task_counts)
        Mct = sum(1 for count in task_counts if count == M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)