class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        half_n = int(n/2)
        frequencyDict = {}
        for idx in range(n):
            if nums[idx] not in frequencyDict:
                frequencyDict[nums[idx]] = 1
                if frequencyDict[nums[idx]] > half_n:
                    return nums[idx]
            else:
                frequencyDict[nums[idx]] +=1
                if frequencyDict[nums[idx]] > half_n:
                    return nums[idx]
            