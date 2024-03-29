class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max = 0
        i = 0
        while i < len(gain):
            alt += gain[i]
            if alt > max:
                max = alt
            i += 1
        return max