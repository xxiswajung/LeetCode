class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if self.empty(): return #push stack & pop stack 둘다 비었으면 pop 중지
        if len(self.output): #pop stack 에 원소가 있다면
            return self.output.pop() #pop
        else: # pop stack 에만 q 원소가 없다
            while len(self.input):
                self.output.append(self.input.pop())
        return self.output.pop()


    def peek(self) -> int:
        if self.empty(): return
        if len(self.output):
            return self.output[-1]
        else:
            while len(self.input):
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        if self.input or self.output:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()