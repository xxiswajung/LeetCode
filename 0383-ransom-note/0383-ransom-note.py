class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in ransomNote:
            if ransomNote.count(x)>magazine.count(x):
                return False
        return True