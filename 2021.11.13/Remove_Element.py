#https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        num_re = 0      #紀錄有幾個重複
        i = 0
        while i < n - num_re:   #當去除重複的時候，nums變短，所以迴圈就要少跑
            if nums[i] == val:
                nums.remove(nums[i])
                num_re += 1
            else:
                i = i +1
        return n - num_re
        

