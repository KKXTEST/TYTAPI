# -*- coding: utf-8 -*-
# @Author  : Alan
# @Time    : 2022/5/10 11:11
# @File    : testvcode.py
# @Descr   :

import flask
import pymysql

api = flask.Flask(__name__)

MYSQL_INFO_DEV = {
    'host': 'rm-2ze9tpg20pz7ymzvwoo.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'tyt_dev',
    'password': 'tyt_dev#20200724',
    'db': 'tyt'
}

MYSQL_INFO_TEST = {
    'host': 'rm-2ze4m8jj53967hs09yo.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'tyt_test',
    'password': 'tyt_testDB_20200608',
    'db': 'tyt'
}
MYSQL_INFO_RELEASE = {
    'host': 'rm-2zex5216487f9y92g.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'tyt_write',
    'password': 'Tyt_write',
    'db': 'tyt'
}
SQL = "SELECT phone,verify_code FROM tyt.tyt_verify_log ORDER BY id DESC LIMIT 5"


def select_db(sql, dbinfo):
    conn = pymysql.connect(**dbinfo)
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    if res is not None:
        res = res
    else:
        res = None
    cursor.close()
    conn.close()
    return res


def result(sel):
    if sel:
        res = {'msg': sel, 'code': 200}
    else:
        res = {'msg': "查询失败", 'code': 201}
    return res


@api.route('/<env>/code')
def environment(env):
    info = "MYSQL_INFO_"+str(env).upper()
    return result(select_db(SQL, eval(info)))


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=5000, debug=True)