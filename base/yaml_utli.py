#ecoding:utf-8
import yaml
import os
class yamlfunc:
#读取yaml文件
    def read_yaml():
        with open(os.path.abspath('../config/')+"/basic.yaml",wd='r',encoding='utf-8')as f:
            yaml.load(stream=f,Loader=yaml.FullLoader)

#写入yaml文件
    def write_yaml(self,data):
        with open(os.path.abspath('../config/')+'write.yaml',mode='a',encoding='utf-8')as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)
#清除yaml文件
    def clear_yaml(self,data):
        with open(os.path.abspath('../config/')+'/write.yaml',mode='w',encoding='utf=8')as f:
             f.truncate()
            