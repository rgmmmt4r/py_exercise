class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n > 0:
            if(n %2 ==1):
                sum += 1
            n = int(n/2)
        return sum