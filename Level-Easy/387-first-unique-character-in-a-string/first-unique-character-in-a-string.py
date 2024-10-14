from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sCounter = Counter(s)
        for i, count in sCounter.items():
            if count == 1:
                return s.index(i)
        return -1
        
        