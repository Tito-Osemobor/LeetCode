class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in visited:
                return False
            visited.add(n)
        return True