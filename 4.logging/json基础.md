<!--
 * @Descripttion: 
 * @version: 
 * @Author: sch
 * @Date: 2022-03-14 11:29:44
 * @LastEditors: sch
 * @LastEditTime: 2022-03-14 11:44:32
-->
# 1. 类型转换
## 1.1 Python -> Json
<font color="orange" size="4">

1. dict -> object
2. list, tuple -> array
3. str -> string
4. int, float -> number
5. True -> true
6. False -> false
7. None -> null

</font>

## 1.2. Json -> Python
<font color="orange" size=“4”>

1. object -> dict
2. array -> list
3. string -> str
4. number (int) -> int
5. number (float) -> float
6. true ->True
7. false -> False
8. null -> None

</font>


# 2. 使用方法
<font color="orange" size="4">

1. `json.dump(obj, fp)`: 将Python数据类型转换并保存到 json 格式的文件
2. `json.dumps(obj)`: 将Python数据类型转换为 json 格式的字符串
3. `json.load(fp)`: 从json格式的文件中读取数据转换为 Python 类型
4. `json.loads(s)`: 将json格式的文件转换为Python类型 

</font>