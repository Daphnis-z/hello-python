#! /bin/bash
# -*- sh -*-

# 获取程序的根目录，便于对资源进行定位
PRG="$0"
while [ -h "$PRG" ]; do
        ls=`ls -ld "$PRG"`
        link=`expr "$ls" : '.*-> \(.*\)$'`
        if expr "$link" : '.*/.*' > /dev/null; then
                PRG="$link"
        else
                PRG=`dirname "$PRG"`/"$link"
        fi
        done
PRGDIR=`dirname "$PRG"`
cd $PRGDIR/..

root_dir=`pwd`

# 创建程序所需的目录
mkdir "logs"

# 创建软连接
cd ..
rm -rf hello-python
ln -s $root_dir hello-python
