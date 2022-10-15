#TLE
import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest_str = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1,1):
                if self.isPalindrome(s[i:j]):
                    if len(s[i:j]) > len(largest_str):
                        largest_str = s[i:j]


        return largest_str
    def isPalindrome(self,s) -> bool:
        for i in range(math.floor(len(s)/2)):
            if s[len(s)-i-1] != s[i]:
                return False
        return True

s = Solution()

print(s.longestPalindrome("caba"))
