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

# 获取程序根目录的绝对路径
root_dir=`pwd`

echo "program root dir: $root_dir"

# 启动程序
python3 $root_dir/hello-python/main.py
