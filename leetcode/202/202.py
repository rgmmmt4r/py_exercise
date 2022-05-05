class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(n:int) -> int:
            num = 0
            n = str(n)
            for i in range(len(n)):
                num += int(n[i])**2
            return num
        appearance_set = set()
        this_round_num = calculate(n)
        while(this_round_num!= 1):
            if this_round_num not in appearance_set:
                appearance_set.add(this_round_num)
            else:
                return False
            this_round_num = calculate(this_round_num)
        return True
        




s = Solution()

print(s.isHappy(19))