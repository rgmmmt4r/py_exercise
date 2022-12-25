class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while  True:
            if n == 1:
                break
            if n %2 != 0:
                return False
            n = n/2
        return True