#題目：https://leetcode.com/problems/two-sum/
#輸入array 並且轉成list[int]
input_string = input()
nums_list = input_string.split()
for i in range(len(nums_list)):
    nums_list[i] = int(nums_list[i])

target = int(input())
answer = []

#用雙層for迴圈窮舉找出答案
for i in range(len(nums_list)):
    for j in range(1,len(nums_list)-1):
        if nums_list[i] + nums_list[j] == target:
            answer = [i , j]
        else:
            j = j + 1
print(answer)