class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr=encoding
        
    def next(self, n: int) -> int:
        num=-1
        while self.arr and n>0:
            if n<=self.arr[0]:
                self.arr[0]-=n
                n=0
                num=self.arr[1]
            else:
                n-=self.arr[0]
                self.arr[0]=0
            if self.arr[0]==0:
                self.arr.pop(0)
                self.arr.pop(0)

        return num


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)