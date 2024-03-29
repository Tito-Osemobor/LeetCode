class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(0, n):
            freq = {}
            max_freq = 0
            for j in range(i, n):
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1
                max_freq = max(max_freq, freq[s[j]])
                min_freq = min(freq.values())
                ans += (max_freq - min_freq)
        return ans