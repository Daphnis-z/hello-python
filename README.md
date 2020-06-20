# hello-python
It is a python project template,contains config,log,linux run script so on..



# 前言

准备做一个 Python 的项目模板，包含 **配置文件**、**程序日志**、**Linux 运行脚本** 等，后面把项目上值得固化的东西也放上来。

因为现在项目一般都是基于 **Python3** 的，所以这个模板暂时也不考虑兼容 Python2。



# 目录介绍

按 github 上的顺序从上往下介绍顶级目录，次级目录就不介绍了。

- **bin**

  存放一些执行脚本，比如 程序配置、启动、停止脚本。

- **data**

  存放一些本地数据文件。

- **docs**

  存放一些项目文档。

- **etc**

  存放项目配置文件。

- **hello-python**

  程序所有的源码，包括测试代码，都放到这个下面。



# 涵盖内容

## 1. 配置文件

见 **etc/hello-python.yml** ，目前用 yaml 做配置文件是比较流行的，它结构清晰，支持字符串、数字和数组，程序里面使用 **PyYAML** 来读取 yaml 。

## 2. 日志系统

目前使用的是 Python 自带的 **logging** 模块来写日志，详情见源码，后面如果有发现比较不错的第三方库再进行替换。

## 3. 项目打包

使用 setup.py 进行打包，目前支持打包成 tar.gz 的格式，可以直接拿到 Linux 上安装运行。

打包命令如下：

```
python setup.py sdist
```

打包的时候需要一起复制过去的文件都写到 **MANIFEST.in** 里面即可。

## 4. 项目依赖

**requirements.txt** 里面存放着项目依赖的三方包和版本，在新环境上安装依赖，执行下面的命令即可：

```
pip3 install -r requirements.txt
```

## 5. Linux 脚本

- **config.sh**

  程序配置脚本，可以在里面创建软连接、目录等。

- **run-hello-python.sh**

  程序执行脚本，支持前台和后台两种运行模式：

  ```shell
  # 前台运行
  bash bin/run-hello-python.sh
  
  # 后台运行
  bash bin/run-hello-python.sh -d
  ```

- **stop-hello-python.sh**

  当程序后台执行时，可以使用该脚本快速停止程序。

# 安装运行

Windows 上就不讲了，现在的项目一般都跑在 Linux 上。

## 1. 打包

在程序根目录下打开命令行窗口，执行下面的命令：

```shell
python setup.py sdist
```

打包成功后会在 **dist** 目录下生成 **hello-python-1.0.0.tar.gz** 安装包。

## 2. 安装

把安装包上传到程序的安装目录，然后执行下面的命令：

```shell
# 解压安装包
tar -zxvf hello-python-1.0.0.tar.gz

# 执行配置脚本
bash hello-python-1.0.0/bin/config.sh
```

## 3. 执行

进到程序根目录，检查下 **logs** 目录有没有正常创建，没有就手动创建一下。然后使用下面的命令启动程序：

```shell
bash bin/run-hello-python.sh
```

