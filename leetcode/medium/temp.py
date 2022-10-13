num1, num2 = 0,0
str1 = "321"
str2 = "123"

for i in range(len(str1)):
    num1 += (int(str1[len(str1)-1-i]) * (10**(len(str1)-1-i)))
for j in range(len(str2)):
    num2 += (int(str1[len(str2)-1-j]) * (10**(len(str2)-1-j)))
print(num1)
print(num2)