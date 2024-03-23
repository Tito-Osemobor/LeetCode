class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        while(k > min(nums)):
            nums.remove(min(nums))
            count += 1
        return count