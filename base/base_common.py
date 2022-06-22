# -*- coding: utf-8 -*-
# @Author  : Alan
# @Time    : 2022/4/21 9:59
# @File    : read_ini.py
# @Descr   : 基类调用登录接口登录操作


from base.read_yaml import read_host_yaml
from base.read_yaml import read_basic_yaml
from base.api_data import login_api
import requests
class basic():

    @classmethod
    def setupClass(cls):
        print('case执行之前进行的动作')
        # #执行登录操作
        # import requests
        # from base.read_yaml import read_basic_yaml
        # from base.read_yaml import read_host_yaml
        # host=read_host_yaml()["host"][release]
        # api=login_api.apiadd
        # url=host+api
        # data=login_api.data
        # headers=read_basic_yaml()["headers"]
        # method=read_basic_yaml()["method"]["m1"]
        # lorequests=requests.method(url=url,data=data,headers=headers)
        # print(lorequests)
        # # data=read_login_yaml()
        # # print(data)
        # # logindata={}
        # # logindata.update(read_login_yaml(data["login"]))
        # # print(logindata)
        # # dict1=logindata
        # # print(dict1)
        # # print(dict1.keys())
    @classmethod
    def tearDownClass(cls):
        print('用例执行完成后动作')

    def test_login():
         host=read_host_yaml()['host']['release']
         method=read_basic_yaml()['method']['m1']
         print(method)
         api=login_api.apiadd
         url=host+api
         data=login_api.data
         headers = read_basic_yaml()['headers']['header']
         print(url,data,headers)
#判断请求方式是否是大写如果是转换为小写
         method=str(method).lower()
         if method=='post':
             res=requests.models(method)(url=url,data=data,headers=headers)
         else:
             print("请求方式不正确")
         print(res.status_code)
         print(res.request)
         print(res.text)
print(basic.test_login())