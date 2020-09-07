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

11. 避免在循环中用 + 和 += 操作符来累加字符串. 由于字符串是不可变的, 这样做会创建不必要的临时对象, 并且导致二次方而不是线性的运行时间. 作为替代方案, 可以将每个子串加入列表, 然后在循环结束后用 `.join` 连接列表. 

12. 命名约定
    1. 所谓"内部(Internal)"表示仅模块内可用, 或者, 在类内是保护或私有的.
    2. 用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
    3. 用双下划线(__)开头的实例变量或方法表示类内私有.
    4. 将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
    5. 对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.







Python 编码规范： https://www.runoob.com/w3cnote/google-python-styleguide.html  ——ok
