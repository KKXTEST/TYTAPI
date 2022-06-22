#coding:utf-8
import hashlib
import json
from base.read_yaml import read_basic_yaml
from base.api_data import login_api
#取出固定的key
def basic_key():
    key=read_basic_yaml()["signKey"] ["singkey"]
    return key
print(basic_key())
#去掉字典参数中，和：后的空格，然后排序，不按ascii可以显示中文，按字母排序,输出str
def score_dict(data_dic):
    return json.dumps(data_dic, separators=(",", ":"), ensure_ascii=False, sort_keys=True)
#字典按照key排序输入dic
def sorce_dic(data_dic):
    return dict(sorted(data_dic.items(),key=lambda x:x[0],reverse=False))


#加密前字符串组合
def secret_key(data_str,key):
    key=basic_key()
    str=data_str+key
    return str
#md5加密密码
def pwd_md5():
    phonenum=17788556666
    firstpwd=123321
    key=basic_key()
    md5pwd=hashlib.md5(str(phonenum+firstpwd)+key.encode('utf-8')).hexdigest()
    return md5pwd
print(pwd_md5())
#MD5获得sing
def sing_md5():
    data=login_api.data
    sing=hashlib.md5(str(data).encode('utf-8')).hexdigest()
    return sing
print(sing_md5())
# def md5():
#     return hashlib.md5(str(data_str).encode('utf-8')).hexdigest()


# def sing_md5():
#     key=read_basic_yaml()["signKey"] ["singkey"]
#     print(key)
#     data=login_api.data
#     print(data)

#添加秘钥
# def add_secret_key(self, data_str):
#     return data_str +sing_md5(['key'])
# print(add_secret_key())
# def json_file():
#     oldfile=login_api.data
#     newfile=json.load(oldfile)
#     print(newfile)
# print(json_file())
# #去掉字典参数中，和：后的空格，然后排序，不按ascii可以显示中文，按字母排序,输出str
# def data_sort_json(self,data_dic):
#     data_dic=sing_md5()
#     print(data_dic)
#     return json.dumps(data_dic, separators=(",", ":"), ensure_ascii=False, sort_keys=True)
