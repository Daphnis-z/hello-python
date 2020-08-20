from unittest import TestCase

from hello.info.info import Info


class TestInfo(TestCase):
    def test_say(self):
        info = Info()
        self.assertEqual('hello python', info.say())

    def test_func2(self):
        info = Info()
        info.func2()
