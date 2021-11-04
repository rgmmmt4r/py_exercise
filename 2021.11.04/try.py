#輸入數字，每個數字之間都有一個間隔，並且轉成list[int]
input_string = input()
nums_list = input_string.split()
for i in range(len(nums_list)):
    nums_list[i] = int(nums_list[i])



target = int(input())
answer = []

#用雙層for迴圈窮舉找出答案
for i in range(0,len(nums_list)-1):
    #print("i: " + str(i)+ " ")
    for j in range(i+1,len(nums_list)):
        #print("j: " + str(j) + " ")
        if nums_list[i] + nums_list[j] == target:
            answer = [i , j]



print(answer)
