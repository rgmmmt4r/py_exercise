

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        dupli = 0
        i = 0
        while i < n - 1 - dupli:
            k = i
            l = i
            while nums[k] == nums[k+1] and k < n - 1 - dupli:
                dupli += 1
                k = k + 1
                if k == n-1:
                    return n - dupli
            for j in range(k+1,n):
                nums[l+1] = nums[j]
                l = l + 1
            

            while nums[i] != nums[i+1] and i < n - 1 - dupli:
                i = i + 1
                if i == n - 1 - dupli:
                    return n - dupli
        return n - dupli
nums = [1,1,2,2]
s = Solution()
a = s.removeDuplicates(nums)
print(nums)
print(a)
        