class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in set(ransomNote):
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True