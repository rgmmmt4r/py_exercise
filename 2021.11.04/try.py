#輸入數字，每個數字之間都有一個間隔，並且轉成list[int]
while(True):
    input_string = input("請輸入數字，每個數字之間都有一個間隔隔開:")
    nums_list = input_string.split()
    try:
        for i in range(len(nums_list)):
            nums_list[i] = int(nums_list[i])
        break
    except ValueError:
        print("您輸入的不是整數，請重新輸入")

target = int(input("請輸入target:"))
answer = []

#用雙層for迴圈窮舉找出答案
for i in range(0,len(nums_list)-1):
    #print("i: " + str(i)+ " ")
    for j in range(i+1,len(nums_list)):
        #print("j: " + str(j) + " ")
        if nums_list[i] + nums_list[j] == target:
            answer = [i , j]

print(answer)
