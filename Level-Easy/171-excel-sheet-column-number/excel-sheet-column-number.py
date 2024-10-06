class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        for c in columnTitle:
            currentVal = ord(c) - ord('A') + 1
            count = count * 26 + currentVal
        return count