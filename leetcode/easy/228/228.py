class Solution:
    def summaryRanges(self, nums) :
        total_list = []
        i = 0
        j = 0
        while i < len(nums):
            if i +1 < len(nums):
                if nums[i+1] == nums[i] +1:
                    i += 1
                else:
                    i += 1
                    if i == j + 1:
                        total_list.append(str(nums[j]))
                    else:
                        total_list.append(str(nums[j]) + "->" + str(nums[i-1]))
                    j = i
            else:
                i +=1
                if i == j + 1:
                    total_list.append(str(nums[j]))
                else:
                    total_list.append(str(nums[j]) + "->" + str(nums[i-1]))

        return(total_list)


s = Solution()

print(s.summaryRanges([1,4,5]))
