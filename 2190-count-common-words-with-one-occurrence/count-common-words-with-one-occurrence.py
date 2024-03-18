class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans = 0
        for word in filter(lambda x: words1.count(x) == 1, words1):
            if words2.count(word) == 1:
                ans += 1
        return ans
