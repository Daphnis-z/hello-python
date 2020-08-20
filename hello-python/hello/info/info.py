import traceback

from hello import log_util


class Info:
    logger = log_util.get_logger()

    def __init__(self):
        self.name = 'hello'

    def say(self):
        return self.name + ' python'

    def func1(self):
        print('this is func1 ..')
        strs = ['123']
        print(strs[2])

    def func2(self):
        try:
            print('this is func2 ..')
            self.func1()
        except Exception:
            self.logger.error(traceback.format_exc())
