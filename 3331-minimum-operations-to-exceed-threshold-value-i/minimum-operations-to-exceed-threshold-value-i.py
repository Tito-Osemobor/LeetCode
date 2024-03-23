class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len([i for i in nums if i < k])