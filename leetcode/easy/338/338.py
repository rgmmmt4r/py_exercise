# beat 80%
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0]
        for i in range(1,n+1):
            this_ans_for_i = 0
            if i % 2 == 1:
                this_ans_for_i += 1
            this_ans_for_i = ans[int(i/2)] + this_ans_for_i
            ans.append(this_ans_for_i)
        return ans