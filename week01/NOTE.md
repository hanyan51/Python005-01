学习笔记
Number （数字）

String （字符串）

List （列表）

Tuple （元组）

Set （集合）

Dictionary （字典）

不可变的数据类型为：Number, String, Tuple

可变的数据类型为：List, Set, Dictionary

Number 支持 int, float, bool, complex, 内置的 type() 函数可用来查询变量所指的对象类型。

String： 

切片

```python
#获取切片，复数代表倒数第几个，从0开始
>>> name ="little-five"
>>> name[1]
'i'
>>> name[0:-2] #从第一个到倒数第二个，不包含倒数第二个
'little-fi'
```

索引 —>index()、find()

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 修正版
name = "little_five"
#index-->获取索引，语法->str.index(str, beg=0 end=len(string))，第二个参数指定起始索引beg，第三个参数结束索引end，指在起始索引到结束索引之前获取子串的索引
print(name.index("l",2,8)) #在索引区间2-8之前查找‘l’,找到是第二个‘l’,其索引为4

#find -->其作用与index相似
print(name.find("l",2))  #结果也为 4
```

长度 —>len()

```python
name = "little_five"
#获取字符串的长度
print(len(name))

#输出为：
>>> 11
```

删除 —>del

```python
#删除字符串，也是删除变量
>>> name ="little-five"
>>> del name
>>> name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
```

大小写转换 —>capitalize()、lower()、upper()、title()、swapcase()

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

#大小写的互相转换
>>> name ="little_five"
#首字母大写-->capitalize
>>> name.capitalize()
'Little_five'

#转为标题-->title
>>> info ="my name is little_five"
>>> info.title()
'My Name Is Little_Five'

#全部转为小写-->lower
>>> name ="LITTLE_FIVE"
>>> name.lower()
'little_five'

#全部转为大写-->upper
>>> name = "little_five"
>>> name.upper()
'LITTLE_FIVE'

#大小写转换-->swapcase
>>> name ="lIttle_fIve"
>>> name.swapcase()
'LiTTLE_FiVE'
```

判断以什么开头结尾 —>startswith()、endswith()

```python
#判断以什么开头、结尾
>>> name ="little-five"

#判断以什么结尾
>>> name.endswith("e")
True

#判断以什么开头
>>> name.startswith("li")
True
```

扩展 —>expandtabs()     #expandtabs -->返回字符串中的 tab 符号 ('\t') 转为空格后生成的新字符串，通常可用于表格格式的输出。

```python
#expandtabs -->返回字符串中的 tab 符号('\t')转为空格后生成的新字符串。通常可用于表格格式的输出

info ="name\tage\temail\nlittlefive\t22\t994263539@qq.com\njames\t33\t66622334@qq.com"
print(info.expandtabs(10))

#输出为：
name      age       email
little-five         22        994263539@qq.com
james     33        66622334@qq.com
```

格式化输出 —>format()、format_map()

```python
#格式化输出-->format、format_map

#forma方法
#方式一
>>> info ="my name is {name},I'am {age} years old."
>>> info.format(name="little-five",age=22)
"my name is little-five,I'am 22 years old."

#方式二
>>> info ="my name is {0},I'am {1} years old."
>>> info.format("little-five",22)
"my name is little-five,I'am 22 years old."

#方式三
>>> info ="my name is {name},I'am {age} years old."
>>> info.format(**{"name":"little-five","age":22})
"my name is little-five,I'am 22 years old."

#format_map方法
>>> info ="my name is {name},I'am {age} years old."
>>> info.format_map({"name":"little-five","age":22})
"my name is little-five,I'am 22 years old."
```

join 方法

```python
#join--> join(): 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串

#字符串
>>> name ="littefive"
>>> "-".join(name)
'l-i-t-t-e-f-i-v-e'

#列表
>>> info = ["xiaowu","say","hello","world"]
>>> "--".join(info)
'xiaowu--say--hello--world'
```

分割 —> spilit()、partition()

```python
#分割，有两个方法-partition、split

#partition -->只能将字符串分为三个部分，生成列表
>>> name ="little-five"
>>> name.partition("-")
['little', '-', 'five']

#split-->分割字符串，并且可以指定分割几次，并且返回列表
>>> name ="little-five-hello-world"
>>> name.split("-")
['little', 'five', 'hello', 'world']
>>> name.split("-",2)  #指定分割几次
['little', 'five', 'hello-world']
>>>
```

替代 —> replace()

```python
#替代
>>> name ="little-five"
>>> name.replace("l","L")
'LittLe-five'
#也可以指定参数，替换几个
>>> name.replace("i","e",2)
'lettle-feve'
 

#清除空白 --> strip()、lstrip()、rstrip()

#去除空格
>>> name ="  little-five   "

#去除字符串左右两边的空格
>>> name.strip()
'little-five'

#去除字符串左边的空格
>>> name.lstrip()
'little-five   '

#去除字符串右边的空格
>>> name.rstrip()
'  little-five'
```

### 列表

列表是由一系列顺序排列的元素组成的，它的元素可以是任何数据类型，即数字、字符串、列表、元组、字典、布尔值等等，同时其元素也是可修改的。

```python
1 names = [“little-five”,"James","Alex"]
2 #或者
3 names = list([“little-five","James","Alex"])
```

索引、切片

```python
#索引-->从0开始，而不是从一开始
name =["xiaowu","little-five","James"]
print(name[0:-1])

#切片-->负数为倒数第几个，其为左闭右开，如不写，前面表示包含前面所有元素,后面则表示后面所有元素
m1 =name[1:]
print(m1)
#输出为-->['little-five', 'James']
m2 =name[:-1]
print(m2)
#输出为-->['xiaowu', 'little-five']
```

追加 —> append()

```python
#追加元素-->append()
name =["xiaowu","little-five","James"]
name.append("alex")
print(name)

#输出为-->['xiaowu', 'little-five', 'James', 'alex']
```

扩展 —> extend()

```python
#扩展--> 其将字符串或者列表的元素添加到列表内
#一、将其他列表元素添加至列表内
name =["xiaowu","little-five","James"]
name.extend(["alex","green"])
print(name)
#输出为-->['xiaowu', 'little-five', 'James', 'alex', 'green']

#二、将字符串元素添加到列表内
name =["xiaowu","little-five","James"]
name.extend("hello")
print(name)
#输出为-->xiaowu', 'little-five', 'James', 'alex', 'h', 'e', 'l', 'l', 'o']

#三、将字典元素添加至列表内，注：字典的key。
name =["xiaowu","little-five","James"]
name.extend({"hello":"world"})
print(name)
```

追加 append 与扩展 extend 的区别：-->前者为添加将元素作为一个整体添加，后者为将数据类型的元素分解添加至列表内。

```python
#append -->追加
name.append(["hello","world"])
print(name)
输出为 -->['xiaowu', 'little-five', 'James', ['hello', 'world']]

#extend-->扩展
name =["xiaowu","little-five","James"]
name.extend(["hello","world"])
print(name)
输出为-->['xiaowu', 'little-five', 'James', 'hello', 'world']
```

插入 —>insert()

```python
#insert（）插入-->可以指定插入列表的某个位置，前面提到过列表是有序的
name =["xiaowu","little-five","James"]
name.insert(1,"alex") #索引从0开始，即第二个
print(name)
```

取出 —>pop()

```python
#pop()--取出，可将取出的值作为字符串赋予另外一个变量
name =["xiaowu","little-five","James"]
special_name =name.pop(1)
print(name)
print(special_name,type(special_name))

#输出为：['xiaowu', 'James']
#little-five <class 'str'>
```

移除 —>remove()、删除 —>del()

```python
#remove -->移除，其参数为列表的值的名称
name =["xiaowu","little-five","James"]
name.remove("xiaowu")
print(name)

#其输出为：['little-five', 'James']

#del -->删除
name =["xiaowu","little-five","James"]
#name.remove("xiaowu")
del name[1]
print(name)

#其输出为：['xiaowu', 'James']
```

sorted()-->排序，默认正序，加入reverse =True，则表示倒序

```python
#正序
num =[11,55,88,66,35,42]
print(sorted(num)) -->数字排序
name =["xiaowu","little-five","James"]
print(sorted(name)) -->字符串排序
#输出为：[11, 35, 42, 55, 66, 88]
#['James', 'little-five', 'xiaowu']

#倒序
num =[11,55,88,66,35,42]
print(sorted(num,reverse=True))
#输出为：[88, 66, 55, 42, 35, 11]
```

### 元组 tuple 类

元组即为不可修改的列表，其特性与list 相似，使用圆括号而不是方括号来标识。

```python
#元组
name = ("little-five","xiaowu")
print(name[0])
```

### 字典 dict 类

字典为一系列的键-值对，每个键值对用逗号隔开，每个键都与一个值相对应，可以通过使用键来访问对应的值。它是无序的。键的定义必须是不可变的，即可以是数字、字符串也可以是元组，还有布尔值等，而值的定义可以是任意数据类型。

```python
#字典的定义
info ={
    1:"hello world",  #键为数字
    ("hello world"):1, #键为元组
    False:{ 
        "name":"James"
    },
    "age":22
}
```

遍历 -->items、keys、values

```python
info ={
   "name":"little-five",
   "age":22,
   "email":"99426353*@qq,com"
}
#键
for key in info:
    print(key)
print(info.keys())
#输出为：dict_keys(['name', 'age', 'email'])

#键值对
print(info.items())
#输出为-->dict_items([('name', 'little-five'), ('age', 22), ('email', '99426353*@qq,com')])

#值
print(info.values())
#输出为：dict_values(['little-five', 22, '99426353*@qq,com'])
```

### 集合 set 类

集合的特性：

1、去重

2、无序

3、每个元素必须为不可变类型即（hashable类型，可作为字典的key）

```python
#1、创建，将会自动去重,其元素为不可变数据类型，即数字、字符串、元组
test01 ={"zhangsan","lisi","wangwu","lisi",666,("hello","world",),True}
#或者
test02 =set({"zhangsan","lisi","wangwu","lisi",666,("hello","world",),True})

#2、不可变集合的创建 -->frozenset()
test =frozenset({"zhangsan","lisi","wangwu","lisi",666,("hello","world",),True})
```

增加：add / update

```python
#更新单个值 --->add
names ={"zhangsan","lisi","wangwu"}
names.add("james") #其参数必须为hashable类型
print(names)

#更新多个值 -->update
names ={"zhangsan","lisi","wangwu"}
names.update({"alex","james"})#其参数必须为集合
print(names)
```

删除：pop、remove、discard

```python
#随机删除 -->pop
names ={"zhangsan","lisi","wangwu","alex","james"}
names.pop()
print(names)

#指定删除，若要删除的元素不存在，则报错 -->remove
names ={"zhangsan","lisi","wangwu","alex","james"}
names.remove("lisi")
print(names)

#指定删除，若要删除的元素不存在，无视该方法 -->discard
names ={"zhangsan","lisi","wangwu","alex","james"}
names.discard("hello")
print(names)
```
