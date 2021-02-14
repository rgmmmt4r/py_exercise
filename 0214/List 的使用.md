下面是一個List，用於紀錄美金商品價格


```python
L = [10,20,30]
```

假設美金的匯率是 27.5，可以使用for迴圈印出台幣價格，也可以用append放入其他的list


```python
e = 27.5
```


```python
for i in L:
    print(i*e)
```

    275.0
    550.0
    825.0



```python
N = []
```


```python
for i in L:
    twd = i*e
    N.append(twd)
    
```


```python
N
```




    [275.0, 550.0, 825.0]


