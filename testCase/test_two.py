from base import read_excel
import unittest
from base import baseRequest
from common.config import PATH


class TestTwo(unittest.TestCase):

    def test_api(self):
        api = read_excel.read_dataSouce(PATH("../Report/api2.xlsx"))
        base_request = baseRequest.BaseRequest()
        base_request.send_request(api)

