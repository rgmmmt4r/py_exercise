#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#比之前快一點
#我的作法是遇到重複的數字就砍掉，例如遇到[1,1] 就砍掉前項的 1
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        dupli = 0    #代表重複的數字的個數
        i = 0        #i 用於定位出檢查到哪個位置，當nums[i] != nums[i+1]，i 則加1
        while i < n - 1 - dupli:    #由於我的做法是遇到重複的數字就砍掉，所以當計算出dupli當下的數值，即可確認貼完數字後i應該只檢查到哪
            
            if  nums[i] == nums[i+1]:
                dupli = dupli + 1
                nums.remove(nums[i])
            else:
                i = i + 1
            if i ==  n - 1 - dupli:
                return n - dupli

        return n - dupli