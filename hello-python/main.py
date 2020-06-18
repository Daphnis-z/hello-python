import codecs
import os

import yaml


def init():
    """
    做一些初始化操作
    :return:
    """

    # 读取配置文件
    with codecs.open('etc/hello-python.yml', 'r', 'utf-8') as config_file:
        config_data = config_file.read()
    configs = yaml.load(config_data, Loader=yaml.FullLoader)
    print(configs)


def main():
    init()

    print('work dir: ', os.getcwd())

    # change work dir
    # os.chdir("/home/xx/hello")


if __name__ == '__main__':
    main()
