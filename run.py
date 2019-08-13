from testCase import test_one
import unittest
from base import sendMail


def run():
    suite = unittest.TestSuite()
    '添加测试用例'
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_one.TestOne))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    mail = sendMail.SendMail()
    mail.send()

run()


