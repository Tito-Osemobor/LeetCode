from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for c in set(ransomNote):
            if ransomCounter[c] > magazineCounter[c]:
                return False
        return True