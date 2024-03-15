class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = nums.count(val)
        k = 0
        for _ in range(n):
            nums.remove(val)
        return len(nums)