#https://leetcode.com/problems/remove-duplicates-from-sorted-array
#我的做法是遇到重複的數字時，先算出有幾個連續的重複數字，算好後再從下一個不同數字「由後往前貼數字」，把重複的部分蓋掉，
#例如 input: [1,1,1,3,4] -> 將 [3,4] 往前貼兩格，蓋掉 [1,1] 成為 [1,3,4]
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        dupli = 0                   #代表重複的數字的個數
        i = 0                       #i 用於定位出檢查到哪個位置，當nums[i] != nums[i+1]，i 則加1
        while i < n - 1 - dupli:    
            k = i                   #k 用於計算共有幾的連續的重複數字出現
            l = i                   #l 用於定位要從哪邊開始「由後往前貼數字」
            while nums[k] == nums[k+1] and k < n - 1 - dupli:   #計算共有幾的連續的重複數字出現
                dupli += 1
                k = k + 1
                if k == n-1:
                    return n - dupli
            for j in range(k+1,n):          #由後往前貼數字
                nums[l+1] = nums[j]
                l = l + 1          
            while nums[i] != nums[i+1] and i < n - 1 - dupli: #當數字不同時，i 則加1
                i = i + 1
                if i == n - 1 - dupli:
                    return n - dupli
        return n - dupli