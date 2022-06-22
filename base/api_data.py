#coding:utf-8
import time
from base.read_yaml import read_basic_yaml


# def get_now_time(self):
#     # 获取当前的时间戳
#     time_stamp = time.time()
#     # 转换为int类型的13位时间戳
#     time_stam = int(round(time_stamp * 1000))
#     time_new = str(time_stam)
#     return time_new
#
#
# def get_now_ttkn(self, t):
#     t=get_now_time()
#     timeArray = time.localtime(int(t) / 1000)
#     ttkn = time.strftime("%Y.%m.%d-%H:%M:%S", timeArray)
#     return ttkn
# print(get_now_ttkn(get_now_time(time)))
# timestamp = get_now_time()
# ttkn = get_now_ttkn(timestamp)
# print(ttkn)

#验证签名代码
# def post_sign(self, data):
#     secret_key = "1345~opo-4%"
#     dic = {}
#     for i in data:
#         if data[i] != "":
#             dic[i] = data[i]
#     # 转json，去掉，和：后的空格，不按ascii可以显示中文，按字母排序
#     json_data = json.dumps(dic, separators=(",", ":"), ensure_ascii=False, sort_keys=True)
#     str_data = json_data + secret_key
#     md = hashlib.md5()
#     md.update(str_data.encode('utf-8'))
#     sign = md.hexdigest()
#     return sign
#
#
# def get_sign(self, param):
#     secret_key = "1345~opo-4%"
#     # 将键按照字典序排序
#     sort_param = sorted(param.items(), key=lambda x: x[0], reverse=False)
#     # 将列表转化为字典
#     dic_param = dict(sort_param)
#     dic = {}
#     for i in dic_param:
#         if dic_param[i] != "":
#             dic[i] = dic_param[i]
#     new_param = '&'.join(["{}={}".format(k, v) for k, v in dic.items()])
#
#     str_param = new_param + secret_key
#     # 创建md5对象
#     m = hashlib.md5()
#     m = hashlib.md5(str_param.encode('utf-8'))
#     sign = m.hexdigest()
#     # 将小写字母切换为大写字母
#     return sign
time=time.strftime("%Y-%m-%d-%H:%M:%S")
#print(time)
class login_api():
    apiadd="plat/plat/user/login"
    #data="cellPhone=17788556666&certificateType=0&channelCode=1&cid=1104a8979274946efd9&clientId=1104a8979274946efd9&clientSign=22&clientVersion=6131&deviceId=1104a8979274946efd9&goodsDeviceId=1104a8979274946efd9&osVersion=10&password=a058f0a8d58fb095a7a4f12a89c85cc7&phoneType=PBDT00&sign=13eeed6c214b8cd6b012dc2ccc7b898f&ttkn="
    data={
    "cellPhone": 17788556666,
    "certificateType": 0,
    "channelCode": 1,
    "cid": "1104a8979274946efd9",
    "clientId": "1104a8979274946efd9",
    "clientSign": 22,
    "clientVersion": 6131,
    "deviceId": "1104a8979274946efd9",
    "goodsDeviceId": "1104a8979274946efd9",
    "osVersion": 10,
    "password": "a058f0a8d58fb095a7a4f12a89c85cc7",
    "phoneType": "PBDT00",
    "ttkn": time
    }
#print(login_api.apiadd,login_api.data)
   
class carinfo:
    apiadd="/plat/plat/carNew/identity/get.action"
    data={
    "userId":1001000416,
    "ticket":"6aa47adb5c324098adbd22fbb209b0ee",
    "clientSign":22,
    "clientVersion":6131,
    "osVersion":11,
    "clientId":"190e35f7e0b221e19f6"
     }

class dchyxtx():
     apiadd = "/insurance/cpic.html?needlogin=yes&payStatus=0&"
     data = "clientSign=22&osVersion=11&clientId=190e35f7e0b221e19f6&clientVersion=6131&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&clientSign=22&osVersion=11&clientId=190e35f7e0b221e19f6&clientVersion=6131&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&path=homePage2banner&"
class qnx():
     apiadd ="/insurance/yearly.html?needlogin=yes&payStatus=0&"
     data = "clientSign=22&osVersion=11&clientId=190e35f7e0b221e19f6&clientVersion=6131&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&clientSign=22&osVersion=11&clientId=190e35f7e0b221e19f6&clientVersion=6131&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&path=homePage2banner&"

class tbjl():
    apiadd = "/htbx/insWarrantyList.html?piccType=1&"
    data = "clientSign=22&osVersion=11&clientId=190e35f7e0b221e19f6&clientVersion=6131&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&clientSign=22&osVersion=11&clientId=190e35f7e0b221e19f6&clientVersion=6131&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&path=homePage2banner&"
class tbjldzf():
    apiadd = "/owers_api/transport/insurance/get/list?"
    data ="piccType=1&clientSign=22&clientVersion=6131&clientId=190e35f7e0b221e19f6&osVersion=11&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&lastId=0&opt=1"
    full=apiadd+data
class tbjlsxz():
    apiadd = "/owers_api/transport/insurance/get/list?"
    data ="piccType=1&clientSign=22&clientVersion=6131&clientId=190e35f7e0b221e19f6&osVersion=11&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&lastId=0&opt=2"
    full=apiadd+data
class tbjlysx():
    apiadd = "/owers_api/transport/insurance/get/list?"
    data = "piccType=1&clientSign=22&clientVersion=6131&clientId=190e35f7e0b221e19f6&osVersion=11&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&lastId=0&opt=3"
    full=apiadd+data
class tbjlqb():
    apiadd = "/owers_api/transport/insurance/get/list?"
    data = "piccType=1&clientSign=22&clientVersion=6131&clientId=190e35f7e0b221e19f6&osVersion=11&userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&lastId=0&opt=0"
    full=apiadd+data
class dcxtjbd():
   apiadd="/owers_api/transport/insurance/cpic/add"
   data="userId=1001000416&ticket=6aa47adb5c324098adbd22fbb209b0ee&clientSign=22&clientVersion=6131&osVersion=11&clientId=190e35f7e0b221e19f6&cellPhone=17788556666&type=4&startPoint=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA&destPoint=%E9%99%95%E8%A5%BF%E8%A5%BF%E5%AE%89%E5%B8%82%E6%9C%AA%E5%A4%AE%E5%8C%BA&startTime=1650816000000&startProvinc=%E5%8C%97%E4%BA%AC&startCity=%E5%8C%97%E4%BA%AC%E5%B8%82&startArea=%E6%B5%B7%E6%B7%80%E5%8C%BA&destProvinc=%E9%99%95%E8%A5%BF&destCity=%E8%A5%BF%E5%AE%89%E5%B8%82&destArea=%E6%9C%AA%E5%A4%AE%E5%8C%BA&applicantType=1&applicantName=%E5%95%A6%E5%95%A6%E5%95%A6%E5%95%A6&applicantPhone=17777777888&tsOrderNo=20220500000001&headNo=%E5%86%80C23344&tailNo=%E5%86%80D24555&taskContent1=%E5%8F%98%E5%8E%8B%E5%99%A8&transferStation1=%E6%B2%B3%E5%8C%97%E4%BF%9D%E5%AE%9A%E5%B8%82%E8%8E%B2%E6%B1%A0%E5%8C%BA"
