class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = [[] for _ in range(max(count.values()))]
        for n, c in count.items():
            while c:
                res[c-1].append(n)
                c -= 1
        return res