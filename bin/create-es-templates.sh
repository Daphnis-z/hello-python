#! /bin/bash
# -*- sh -*-

# 获取程序的根目录，便于对资源进行定位
PRG="$0"
while [ -h "$PRG" ]; do
  ls=$(ls -ld "$PRG")
  link=$(expr "$ls" : '.*-> \(.*\)$')
  if expr "$link" : '.*/.*' >/dev/null; then
    PRG="$link"
  else
    PRG=$(dirname "$PRG")/"$link"
  fi
done
PRGDIR=$(dirname "$PRG")
cd $PRGDIR/..

# 获取程序根目录的绝对路径
root_dir=$(pwd)

echo "program root dir: $root_dir"


template_file="demo-data-template.json"
template_name=${template_file%.*}

es_template=`cat etc/es-templates/$template_file`
curl -XPOST -H "Content-Type:application/json" http://127.0.0.1:9200/_template/$template_name -d "$es_template"

