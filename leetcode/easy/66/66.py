class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = "".join(str(e) for e in digits)
        #print(number)
        number = int(number)
        number += 1
        number = str(number)
        digits = []
        for i in range(len(number)):
            digits.append(number[i])
        return digits

s = Solution()

print(s.plusOne([1,2,3]))