class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_t = sum(map(ord, t))
        sum_s = sum(map(ord, s))
        additional_char = chr(sum_t - sum_s)
        
        return additional_char