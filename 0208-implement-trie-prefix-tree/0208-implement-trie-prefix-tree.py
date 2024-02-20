class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        current=self.trie
        
        for s in word:
            if s not in current:
                current[s]={}
            current=current[s]
        current['*'] = True

    def search(self, word: str) -> bool:
        current=self.trie
        
        for s in word:
            if s not in current:
                return False
            current=current[s]
        
        if '*' in current:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current=self.trie
        
        for s in prefix:
            if s not in current:
                return False
            current=current[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)