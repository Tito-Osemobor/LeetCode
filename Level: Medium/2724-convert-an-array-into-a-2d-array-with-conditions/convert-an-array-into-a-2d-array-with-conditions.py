class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        high = max(count.values())
        res = [[] for _ in range(high)]
        for n, c in count.items():
            while c:
                res[c-1].append(n)
                c -= 1
        return res