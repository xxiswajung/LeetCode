class Logger:

    def __init__(self):
        self.mes=defaultdict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mes:
            self.mes[message]=timestamp
            return True
        else:
            if abs(self.mes[message]-timestamp)>=10:
                self.mes[message]=timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)