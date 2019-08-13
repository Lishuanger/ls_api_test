import xlrd


def read_dataSouce(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    row_num = table.nrows
    row_array = []
    i = 1
    while i < row_num:
        row_dic = {}
        row_dic['name'] = table.row(i)[0].value
        row_dic['url'] = table.row(i)[1].value
        row_dic['method'] = table.row(i)[2].value
        row_dic["params"] = table.row(i)[3].value
        row_dic['Assert'] = table.row(i)[4].value
        row_dic['content'] = table.row(i)[5].value
        row_dic['hope'] = table.row(i)[6].value
        row_array.append(row_dic)
        i = i + 1
    return row_array

