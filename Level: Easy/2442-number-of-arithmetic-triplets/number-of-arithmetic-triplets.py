class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        seen=set()
        for i in nums:
            seen.add(i)
        for i in seen:
            if i - diff in seen and i + diff in seen:
                count += 1
        return count