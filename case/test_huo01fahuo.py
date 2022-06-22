#coding:utf-8
import pytest
import requests
import time
import yaml
from base.read_yaml import read_basic_yaml
from base.read_yaml import read_host_yaml
#from base.base_common import basic
from base.api_data import dchyxtx
class test_baoxian():
    #@pytest.mark.xfail表示该用例直接执行失败不执行该条用例
    #@pytest.mark.parametrize('caseinfo',yamlread())
    def dchyx(self):
        #拼接生成URL地址
        #url=args["host"]["release"]+dchyxtx.apiadd
        url=read_host_yaml()["host"]["release"]+dchyxtx.apiadd
        #url=read_host_yaml()["release"]
        method=read_basic_yaml()["method"]["m1"]
        params=dchyxtx.data
        headers=read_basic_yaml()["headers"]
        print(url,params, method,headers)
print(test_baoxian.dchyx.__dict__)
#解开包的用法
#@pytest.mark.parametrize(args,yaml.read()):
#json data格式的传递参数不一样