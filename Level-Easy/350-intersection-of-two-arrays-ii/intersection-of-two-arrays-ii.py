from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=Counter(nums1)
        count2=Counter(nums2)

        intersection = []
        for num in count1:
            if num in count2:
                min_count = min(count1[num], count2[num])
                intersection.extend([num] * min_count)  # Add the element min_count times
        return intersection
        