1. python 标识符**区分大小写**

2. 以下划线开头的标识符有特殊意义
   - 以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
   - 以双下划线开头的 \__foo 代表类的私有成员;
   - 以双下划线开头和结尾的 __foo\_\_  代表 python 里特殊方法专用的标识，如 \_\_init\_\_() 代表类的构造函数；

3. python 可以同一行显示多条语句，方法是用  ;  分开。

4. Python3 中有六个标准的数据类型

   - Number（数字） ——**int、float、bool、complex（复数）**
   - String（字符串）
   - List（列表）
   - Tuple（元组）
   - Set（集合）
   - Dictionary（字典）

   其中 **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；

   **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

5. 可以使用 del 删除一些对象的引用。

   ```python
   del var
   del var_a, var_b
   ```

6. 0 和 None 为 false，其余为 true。

7. 不支持switch语句。

8. Dictionary的键必须为不可变的类型，例如字符串、数字、元组。

9. PyCharm 里面设置 Python 文件头

   Editor > File and Code Templates :  Python Script

   ```python
   #!/usr/bin/python3
   """
   @File:   ${NAME}.py
   @Author: daphnis
   @Time:   ${YEAR}-${MONTH}-${DAY} ${HOUR}:${MINUTE}:${SECOND}
   @Desc:   this is a python3 file
   """
   ```

10. 避免在循环中用 + 和 += 操作符来累加字符串. 由于字符串是不可变的, 这样做会创建不必要的临时对象, 并且导致二次方而不是线性的运行时间. 作为替代方案, 可以将每个子串加入列表, 然后在循环结束后用 `.join` 连接列表. 

11. 命名约定
    1. 所谓"内部(Internal)"表示仅模块内可用, 或者, 在类内是保护或私有的.
    2. 用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
    3. 用双下划线(__)开头的实例变量或方法表示类内私有.
    4. 将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
    5. 对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.

12. 查看保留字

    ```python
    >>> import keyword
    >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    ```

13. 做除法时可以用 // 取整

14. 集合运算

    ```python
    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')
    
    print(a)
    
    print(a - b)   # a 和 b 的差集
    print(a | b)   # a 和 b 的并集
    print(a & b)   # a 和 b 的交集
    print(a ^ b)   # a 和 b 中不同时存在的元素
    ```

15. eval(str) ——用来计算在字符串中的有效Python表达式,并返回一个对象

16. in 和 not in

​		in: 如果在指定的序列中找到值返回 True，否则返回 False。

​		not in: 如果在指定的序列中没有找到值返回 True，否则返回 False。

​	17. is 与 == 区别

​		is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

18. choice(seq): 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。	

19. zfill(width): 返回长度为 width 的字符串，原字符串右对齐，前面填充0

20. Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句，



​		

**参考：**

1. [Python 3 教程](https://www.runoob.com/python3/python3-tutorial.html)

2. [Python 编码规范](https://www.runoob.com/w3cnote/google-python-styleguide.html)









