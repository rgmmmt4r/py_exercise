#題目:https://leetcode.com/problems/pascals-triangle/

main_list = [[1]]   #用於存pascals-triangle
add_list = [1]      #用於for迴圈中加上新的下一層

while(True):
    try:
        n = int(input("請輸入層數，層數請大於等於1層，並且小於31層:")) # n代表層數
        break
    except ValueError:
        print("您輸入的不是整數，請重新輸入")

if n == 1:
    print(main_list)
    quit()
elif n >= 2:
    add_list.append(1)
    main_list.append(list(add_list))

if n == 2:
    print(main_list)
    quit()

#以下只需考慮 n >= 3 的情況
# i 代表main_list需要多加的層數
# j 代表每多加的層中，需要上一層兩個元素相加才能產生的元素個數
for i in range(1,n-1):
    for j in range(1,i+1):
        add_list[j] = main_list[i][j-1] + main_list[i][j]
    add_list.append(1)
    #print("add_list: ")
    #print(add_list)
    main_list.append(list(add_list))
    #print("main_list: " )
    #print(main_list)

print(main_list)
'''
以下是自己寫for迴圈過程中的嘗試
第二層
add_list = [1]
add_list.append(1)
main_list.append(list(add_list))
print(main_list)



第三層
add_list[1] = main_list[1][0] + main_list[1][1]
add_list.append(1)
main_list.append(list(add_list))

第四層
add_list[1] = main_list[2][0] + main_list[2][1]
add_list[2] = main_list[2][1] + main_list[2][2]
add_list.append(1)
main_list.append(list(add_list))
'''

