class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(n:int) -> int:
            num = 0
            n = str(n)
            for i in range(len(n)):
                num += int(n[i])**2
            return num
        appearance_set = set()
        while(calculate(n)!= 1):
            if calculate(n) not in appearance_set:
                appearance_set.add(calculate(n))
            else:
                return False
            n = calculate(n)
        return True
        




s = Solution()

print(s.isHappy(19))