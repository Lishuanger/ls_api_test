import json


def str_equal(hope, res,compare):
    '''
    返回结果是否等于某个字符串
    :param hope: 预期字符串
    :param res: 返回结果
    :param compare: 比较字段
    :return:断言结果
    '''
    data = json.loads(res)
    if hope == data[compare]:
        return "成功"
    else:
        return "失败"



def bool_equal(hope, res,compare):
    '''
    bool结果
    :param hope: 预期结果
    :param res: 返回值
    :param compare: 比较字段
    :return:断言结果
    '''
    data = json.loads(res)

    return '这个不写了，自己扩展方法'


def str_contain(hope, res,compare):
    '''
    返回结果是否包含某个字符串
    :param hope: 预期字符串
    :param res: 返回数据
    :param compare: 比较字段
    :return:断言结果
    '''
    data = json.loads(res)
    if hope in data[compare]:
        return '成功'
    else:
        return '失败'


