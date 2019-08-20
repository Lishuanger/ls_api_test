import xlwt
import xlrd
from xlutils.copy import copy

from common.config import PATH
import os


def write_result(result):
    workbook = xlrd.open_workbook(PATH("../Report/result.xls"))
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)

    i=0
    j = rows_old-1
    print(result)

    while i<len(result):
        item = result[i]
        new_worksheet.write(j+1,0,item['name'])
        new_worksheet.write(j+1,1,item['url'])
        new_worksheet.write(j+1,2,item['params'])
        new_worksheet.write(j+1,3,item['content'])
        new_worksheet.write(j+1,4,item['hope'])
        new_worksheet.write(j+1,6,item['response'])
        new_worksheet.write(j+1,5,item['result'])
        j = j + 1
        i=i+1
        new_workbook.save(PATH("../Report/result.xls"))


