```python
2<3
```




    True




```python
2<=3
```




    True




```python
a = 40
```


```python
(a>50) and (a<100)
```




    False




```python
(a>50) or (a<100)
```




    True




```python
message = ""
while message != "bye" :
    message = input(">>")
    print("拍拍")
```

    >>今天天氣很考
    拍拍
    >>你最近怎麼樣
    拍拍
    >>bye
    拍拍



```python
str = input("美元價格 >>")
str = float(str)
print("{} 美元合台幣{}元".format(str,str*27.5))
```

    美元價格 >>12
    12.0 美元合台幣330.0元



```python
def square(x):
    return x**2
```


```python
a = square(3)
```


```python
a
```




    9



在這邊可以印出a，因為a 被賦予了square(3)


```python
def square2(x):
    print(x**2)
```


```python
b= square2(3)
```

    9



```python
b
```

在這邊不會印出b，因為b 本身沒有數值！！


```python
name = "嘉佑"
place = "台北"
print("來自{}的{}".format(place,name))
```

    來自台北的嘉佑


可以用{} 先空掉要填入的東西，之後再用 .format(place,name) 填入 {}要放入的東西
