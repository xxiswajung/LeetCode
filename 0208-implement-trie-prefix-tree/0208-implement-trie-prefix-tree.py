class Trie:

    def __init__(self):
        self.treelist=[]

    def insert(self, word: str) -> None:
        self.treelist.append(word)

    def search(self, word: str) -> bool:
        for x in self.treelist:
            if x==word:
                return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for x in self.treelist:
            if x[:len(prefix)]==prefix:
                return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)