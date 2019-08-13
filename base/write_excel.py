import xlwt
from common.config import PATH


def write_result(result):
    work_book = xlwt.Workbook(encoding='utf-8')
    sheet = work_book.add_sheet('result')
    title = ['接口名字','api', '参数', '比对字段','预期结果', '比对结果', '接口返回值']
    i = 0
    j = 0
    while i < len(title):
        sheet.write(0, i, title[i])
        sheet.col(i).width = 256 * 30
        i = i + 1

    while j<len(result):
        item = result[j]
        sheet.write(j+1,0,item['name'])
        sheet.write(j+1,1,item['url'])
        sheet.write(j+1,2,item['params'])
        sheet.write(j+1,3,item['content'])
        sheet.write(j+1,4,item['hope'])
        sheet.write(j+1,6,item['response'])
        sheet.write(j+1,5,item['result'])
        j = j + 1
    work_book.save(PATH("../Report/result.xls"))


