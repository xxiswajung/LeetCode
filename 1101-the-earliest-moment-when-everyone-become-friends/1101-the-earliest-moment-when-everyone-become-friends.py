class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        visited=[]
        small_group=[]
        for timestamp, p1, p2 in logs:
            tmp=set()

            if p1 not in visited and p2 not in visited:
                visited.append(p1)
                visited.append(p2)
                tmp.add(p1)
                tmp.add(p2)
                small_group.append(tmp)
            elif p1 in visited and p2 not in visited:
                visited.append(p2)
                for item in small_group:
                    if p1 in item:
                        item.add(p2)
            elif p1 not in visited and p2 in visited:
                visited.append(p1)
                for item in small_group:
                    if p2 in item:
                        item.add(p1)
            else:
                for item in small_group:
                    if p1 in item:
                        a1=item
                    if p2 in item:
                        a2=item
                small_group.append(a1.union(a2))
                small_group.remove(a1)
                
            if {i for i in range(n)} in small_group:
                return timestamp
        return -1
       
            