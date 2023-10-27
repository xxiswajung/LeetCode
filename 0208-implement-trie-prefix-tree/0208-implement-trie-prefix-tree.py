class Trie:

    def __init__(self):
        #self.treelist=[]
        self.root={}
        
    def insert(self, word: str) -> None:
        #self.treelist.append(word)
        cur=self.root
        
        for ch in word:
            if ch not in cur:
                cur[ch]={} #해당 문자로 노드 만들거라고 선언
            cur=cur[ch] #노드의 포인터를 재귀처럼 갱신 = 현재 노드 가리키고 있는 포인터를 노드의 자식을 가리키도록 갱신
        cur['*']=True #단어를 완전하게 삽입 했음을 완료하는 마무리 글자
        
    def search(self, word: str) -> bool:
        # for x in self.treelist:
        #     if x==word:
        #         return True
        # else:
        #     return False
        
        cur=self.root
        
        for ch in word:
            if ch not in cur:
                return False #한글자라도 아니면 나가리
            cur=cur[ch] #포인터 갱신 
        if '*' in cur: #해당 단어가 완전하게 노드에 있으면 true
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        # for x in self.treelist:
        #     if x[:len(prefix)]==prefix:
        #         return True
        # else:
        #     return False
        
        cur=self.root
        
        for ch in prefix: #prefix의 범위가 노드 리스트 안에 있는 단어의 범위보다 작으니까 
            if ch not in cur:
                return False
            cur=cur[ch]
        return True #단어가 완전하게 있을 필요가 없음
        
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)