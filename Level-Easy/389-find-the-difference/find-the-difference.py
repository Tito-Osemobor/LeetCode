class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = sum(ord(i) for i in s)
        ts = sum(ord(i) for i in t)
        return chr(ts - ss)