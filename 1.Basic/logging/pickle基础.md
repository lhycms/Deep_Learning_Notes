<!--
 * @Descripttion: 
 * @version: 
 * @Author: sch
 * @Date: 2022-03-14 10:09:50
 * @LastEditors: sch
 * @LastEditTime: 2022-03-14 11:28:04
-->

<font color="orange" size="4">

- json 是一种通用的数据交换格式和Python的持久化方法之一，只能对基本的一些内置数据类型进行持久化
- `pickle` 模块则是Python专有的持久化模块，甚至可以持久化`自定义的类`，但是 `pickle` 持久化后的字符串是不可读的，不如 json 来得直观，且只能用于 Python环境

</font>

# 1. 主要方法
<font color="red" size="4">

1. `pickle.dumps()` 和 `pickle.loads()` 操作的是 bytes 类型 -- 不可读类型
2. `json.dumps()` 和 `json().loads()` 操作的是 str 类型 -- 可读类型

</font>

<font color="orange" size="4">

1. `pickle.dump(obj, file)`: 将Python数据转换并保存在pickle格式的文件内
2. `pickle.dumps(obj)`: 将Python数据转换为pickle格式的bytes字符串
3. `pickle.load(file)`: 从pickle格式的文件中读取数据转换为Python对象
4. `pickle.loads(bytes_object)`: 将pickle格式的bytes字串转换为Python的类型

</font>


# 2. Demo
## 2.1. Demo 1: `pickle.loads()` 和 `pickle.dumps()` 的使用
```python
>>> import pickle
>>> dic = {"k1": "v1", "k2": 123}
>>> s = pickle.dumps(dic)
>>> s
b'\x80\x04\x95\x16\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x02k1\x94\x8c\x02v1\x94\x8c\x02k2\x94K{u.'
>>> type(s)
<class 'bytes'>
>>> dic2 = pickle.loads(s)
>>> dic2
{'k1': 'v1', 'k2': 123}
```

## 2.2. Demo 2: 写入`pickle`格式的文件
```python
import pickle


data = {
    'a': [1, 2.0, 3, 10];
    'b': ("character string", "byte string")
    'c': {None, True, False}
}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)
```

## 2.3. Demo 3: `pickle.dump()`一个一个写入文件，`pickle.load()`一个一个载入对象
<font color="red" size="4">

Note
----
- dump()方法能一个接着一个地将几个对象转储到同一个文件。随后调用load()可以同样的顺序一个一个检索出这些对象。

</font>

```python
>>> a1 = 'apple'  
>>> b1 = {1: 'One', 2: 'Two', 3: 'Three'}  
>>> c1 = ['fee', 'fie', 'foe', 'fum']  
>>> f1 = open('temp.pkl', 'wb')  
>>> pickle.dump(a1, f1)  
>>> pickle.dump(b1, f1)  
>>> pickle.dump(c1, f1)  
>>> f1.close()  
>>> f2 = open('temp.pkl', 'rb')  
>>> a2 = pickle.load(f2)  
>>> a2  
'apple'  
>>> b2 = pickle.load(f2)  
>>> b2  
{1: 'One', 2: 'Two', 3: 'Three'}  
>>> c2 = pickle.load(f2)  
>>> c2  
['fee', 'fie', 'foe', 'fum']  
>>> f2.close() 
```