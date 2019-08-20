import os
import xlwt
from common.config import PATH


class Config(object):

    def creat_file(self,path):
        if self.check_file(path):
            os.remove(path)
        else:
            pass
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('result')
        title = ['接口名字', 'api', '参数', '比对字段', '预期结果', '比对结果', '接口返回值']
        i = 0
        while i < len(title):
            sheet.write(0, i, title[i])
            sheet.col(i).width = 256 * 30
            i = i + 1
        work_book.save(PATH("../Report/result.xls"))

    def check_file(self, path):
        if not os.path.isfile(path):
            return False
        else:
            return True