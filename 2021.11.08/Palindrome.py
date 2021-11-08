class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)
        if len(x) % 2 == 0:
            for i in range(int(l/2)):
                if x[i] != x[l-1-i]:
                    return False
        else:
            for i in range(int((l+1)/2-1)):
                if x[i] != x[l-1-i]:
                    return False
        return True

s = Solution()
a = s.isPalindrome(-101)
print(a)