from testCase import test_one,test_two
import unittest
from base import sendMail
from base.base_init import Config
from common.config import PATH


def run():
    Config().creat_file(PATH("../Report/result.xls"))
    suite = unittest.TestSuite()
    '添加测试用例'
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_one.TestOne))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_two.TestTwo))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    # mail = sendMail.SendMail()
    # mail.send()

run()


