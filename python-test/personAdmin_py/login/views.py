from django.shortcuts import render
from django.http import HttpResponse
import json
import time

#私有模块
from . import models #创建数据库表的模块
from common.base import resBack, objectTransformDict, getBase64, valuesFun


# 登录
def login(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        user = req_data['user']
        pwd = req_data['pwd']
        result = models.Users.objects.filter(user=user,pwd=pwd)
        if result.count() == 1:
            if result[0].isEnable == 0:
                return resBack(HttpResponse, True, '账号尚未启用!', '')
            else:
                data_1 = getBase64(result[0])
                data_2 = getBase64(int(float(time.time()) * 1000))
                return resBack(HttpResponse, False, '登录成功！', '%s.%s' % (data_1, data_2))
        else:
            return resBack(HttpResponse, True, '账号或密码错误!', '')
    else:
        return HttpResponse('请求错误！')


