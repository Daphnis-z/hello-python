import codecs
import os
from time import sleep

import yaml

from hello.log_util import get_logger

logger = get_logger()


def init():
    """
    做一些初始化操作
    :return:
    """
    logger.info('start init hello python ..')

    # 读取配置文件
    with codecs.open('etc/hello-python.yml', 'r', 'utf-8') as config_file:
        config_data = config_file.read()
    configs = yaml.load(config_data, Loader=yaml.FullLoader)
    logger.info('configs: {}'.format(configs))


def main():
    logger.info('hello python is start ..')
    logger.info(('work dir: ', os.getcwd()))

    init()

    while True:
        logger.info('sleep 10 seconds ..')
        sleep(10)
    # change work dir
    # os.chdir("/home/xx/hello")


if __name__ == '__main__':
    main()
