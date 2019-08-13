import requests
from base.assist import str_equal,str_contain,bool_equal
from base.write_excel import write_result
from common.baseEnum import Mode


class BaseRequest():

    def send_request(self,api):
        '''
        网络请求，该方法只实现了get和post请求
        :param api: api数组
        :return:
        '''

        res = requests.session()
        #实现跨请求保存参数
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "content-type": "application/json;charset=utf-8"}
        res.headers.update(header)

        result = []
        i = 0
        while i < len(api):
            item = api[i]
            url = api[i]["url"]
            params = api[i]["params"]
            method = api[i]["method"]
            req = {}
            if method == "get":
                req = res.get(url=url, params=params)
                item["response"] = req.text
            elif method == "post":
                req = res.post(url=url, json=params)
                item["response"] = req.text

            dic = self.check_results(item,req.text)

            result.insert(i, dic)
            i = i + 1
        write_result(result)

    def check_results(self,item,response):
        '''
        根据assert字段判断对应的断言方法
        :param item: api请求包含信息
        :param response: 请求返回信息
        :return: 测试结果
        '''

        if item['Assert'] == Mode.Equal.value:
            result = str_equal(item['hope'], response, item['content'])
            item['result'] = result
        elif item['Assert'] == Mode.Contain.value:
            result = str_contain(item['hope'], response, item['content'])
            item['result'] = result
        elif item['Assert'] == Mode.Bool.value:
            result = bool_equal(item['hope'], response, item['content'])
            item['result'] = result
        else:
            print("待补充")

        return item
