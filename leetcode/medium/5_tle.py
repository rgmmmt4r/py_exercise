#TLE
import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest_str = ""
        largest_len = 0
        i = 0
        while(len(s) - i >= largest_len):
            for j in range(len(s),i,-1):
                if self.isPalindrome(s[i:j]):
                    if len(s[i:j]) > len(largest_str):
                        largest_str = s[i:j]
                        largest_len = len(largest_str)
                        break
            i = i + 1


        return largest_str
    def isPalindrome(self,s) -> bool:
        for i in range(math.floor(len(s)/2)):
            if s[len(s)-i-1] != s[i]:
                return False
        return True

s = Solution()

print(s.longestPalindrome("abaaa"))
