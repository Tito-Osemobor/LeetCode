class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if (num in dict) and (abs(dict[num] - i) <= k):
                return True
            else:
                dict[num] = i
        return False


        