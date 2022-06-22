# -*- coding: utf-8 -*-
# @Author  : Alan
# @Time    : 2022/4/21 9:59
# @File    : read_yaml.py
# @Descr   : 读取yaml文件
import yaml
import os
#开始读取yaml文件
#第一种方法
def read_basic_yaml():#打开yaml文件
    with open(os.path.abspath('../config/')+"/basic.yaml", encoding='utf-8')as f:
         yamldata=yaml.load(f.read(),Loader=yaml.FullLoader)
         return yamldata
    for method in read_basic_yaml():
        print(read_basic_yaml())["method"]
#第二种方法
def yaml_read2():
    #两个参数 文件路径和加载参数
    #文件流打开方式
    with open('../config/basic.yaml',encoding='utf-8')as f:
    #yaml.load('文件流','加载方式')
         data=yaml.load(f,Loader=yaml.FullLoader)
         return data
    
def read_host_yaml():
    with open("../config/host.yaml",encoding='utf-8')as f:
         hostdata=yaml.load(f.read(),Loader=yaml.FullLoader)
         return hostdata
         # #读取hostyaml文件
         # print(yamldata["host"])
         # #读取test的
         # print(yamldata["host"]["test"])
         # # 读取dev的
         # print(yamldata["host"]["dev"])
         # # 读取release的
         # print(yamldata["host"]["release"])
         # #读取所有请求方法
         # # print(yamldata["method"])
         # # for i in yamldata["method"]:
         # #     print(i)
         # get=yamldata["method"]["m0"]
         # post=yamldata["method"]["m1"]
         # put=yamldata["method"]["m2"]
         # delete=yamldata["method"]["m3"]
         # print(get,post,put,delete)
         # #读取headers
         # headers=yamldata["headers"]
         # print(headers)




         # print(yamldata["method"]["m0"])
         # print(yamldata["method"]["m1"])
         # print(yamldata["method"]["m2"])
         # print(yamldata["method"]["m3"])
         
         #转换为列表
         #创建一个空列表

    #      #print(yamldata.keys())
    #      #拆分key和value
    #      keys=yamldata.keys()
    #      #print(yamldata.values())
    #      values=yamldata.values()
    #      #分别打印key和value
    #      print(keys,values)
    #      # print(values["test"])
    #      # print(values["dev"])
    #      # print(values["release"])
    #      #转换为列表
    #      listkey=list(keys)
    #      listvalues=list(values)
    #      print(listkey,listvalues)
    #      print(len(listvalues))
    #      #拆分字典
    #      host=listvalues[0]
    #      print(type(host))
    #      for i in dict(host).keys():
    #          print(i)
    #      for  v in dict(host).values():
    #          print(v)
    #      listhost=list(dict(host).values())
    #      print(listhost)
    # testhost = listhost[0]
    # devhost = listhost[1]
    # relhost = listhost[2]
    # print(testhost,devhost,relhost)
if __name__=='__main__':
    print(read_basic_yaml())
    print(read_host_yaml()["host"]["release"])
        

