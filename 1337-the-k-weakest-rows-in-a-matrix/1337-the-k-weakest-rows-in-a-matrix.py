class Solution(object):
    def kWeakestRows(self, mat, k):
        arr=[]
        arr2=[]
        for idx, val in enumerate(mat):
            arr.append((idx,sum(val)))
        arr.sort(key=lambda x:x[1])
        for idx, val in (arr):
            arr2.append(idx)
        return arr2[:k]
            
        