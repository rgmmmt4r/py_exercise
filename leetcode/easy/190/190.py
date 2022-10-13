class Solution:
    def reverseBits(self, n: int) -> int:
        normalBits =   bin(n)[2:].zfill(32)
        reverse = ''
        for i in range(len(normalBits)):
            reverse += normalBits[len(normalBits)-1-i]
        return int(reverse,2)
s = Solution()
print(s.reverseBits(123))