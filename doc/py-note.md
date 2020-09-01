1. python 标识符**区分大小写**
2. 以下划线开头的标识符有特殊意义
   - 以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
   - 以双下划线开头的 \__foo 代表类的私有成员;
   - 以双下划线开头和结尾的 __foo\_\_  代表 python 里特殊方法专用的标识，如 \_\_init\_\_() 代表类的构造函数；

3. python 可以同一行显示多条语句，方法是用  ;  分开。

4. Python 有五种标准的数据类型：

   - Numbers（数字）

   - String（字符串）

   - List（列表）

   - Tuple（元组），不能二次赋值

   - Dictionary（字典）

5. 可以使用 del 删除一些对象的引用。

6. 0和null为false，其余为true。

7. 不支持switch语句。

8. 数据类型的值是不允许改变的，这意味着如果改变一个Number数据类型的值将会重新分配内存空间。

9. Dictionary的键必须为不可变的类型，例如字符串、数字、元组。

10. PyCharm 里面设置 Python 文件头

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



Python 编码规范： https://www.runoob.com/w3cnote/google-python-styleguide.html

