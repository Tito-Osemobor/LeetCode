class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = sum(arr)
        for i in range(0, len(arr) - 2):
            j = i + 3
            while j <= len(arr):
                total += sum(arr[i:j])
                j += 2
        return total