class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        num_dict ={}
        for i in range(m):
            if nums1[i] not in num_dict:
                num_dict[nums1[i]] = 1
            else:
                num_dict[nums1[i]] +=1
        for i in range(len(nums2)):
            if nums2[i] not in num_dict:
                num_dict[nums2[i]] = 1
            else:
                num_dict[nums2[i]] +=1

        num_items = num_dict.items()

        sorted_items = sorted(num_items)

        k = 0
        for i in range(len(sorted_items)):
            for j in range(sorted_items[i][1]):
                nums1[k] =  sorted_items[i][0]
                k +=1
        # print(nums1)



s = Solution()

s.merge([1,2,3,0,0,0],3,[2,5,6],3)



# a_dictionary = {4: 2, 3: 3, 2: 1}

# dictionary_items = a_dictionary.items()
# # Get key-value pairs


# sorted_items = sorted(dictionary_items)
# # Sort dictionary by key


# print(sorted_items)
# # OUTPUT