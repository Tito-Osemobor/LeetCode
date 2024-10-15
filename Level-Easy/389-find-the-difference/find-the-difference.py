from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCounter = Counter(s)
        tCounter = Counter(t)

        sCounter.subtract(tCounter)

        difference = "".join(char for char, count in sCounter.items() if count < 0)
        return difference