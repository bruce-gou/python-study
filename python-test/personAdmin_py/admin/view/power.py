from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import admin.model.power as models #创建数据库表的模块
import admin.model.menu as menuModels
from common.base import resBack, valuesFun, getToken

# 查询菜单
def getAllPower(req):
    token = getToken(req)
    if req.method == "GET":
        data = valuesFun(models.Power.objects.filter(userTypeId=token['role']).values())
        if token['role'] != 1:
            for x in data:
                if x['menuName'] == '权限管理' and x['power'].find('编辑') >= 0:
                    x['power'] = '查询'
        return HttpResponse(json.dumps(data),'utf-8',200)

# 查询用户权限列表
def List(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        # 菜单
        menu = valuesFun(menuModels.Menu.objects.all().values())
        for i in menu:
            allPower = i.get('allPower')
            if len(allPower) > 0:
                allPower = allPower.split(',')
            else:
                allPower = []
            i['allPower'] = allPower
        # 权限
        power = models.Power.objects.filter(userTypeId=id).values()
        for i in power:
            allPower = i.get('power')
            if len(allPower) > 0:
                allPower = allPower.split(',')
            else:
                allPower = []
            i['power'] = allPower
        # 数据处理
        for x in menu:
            x['power'] = []
            for y in power:
                if x['id'] == y['menuId']:
                    x['power'] = y['power']
        return HttpResponse(json.dumps(menu),'utf-8',200)
# 权限编辑
def Edit(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        menuId = req_data['menuId']
        menuName = req_data['menuName']
        power = req_data['power']
        power = ','.join(power)
        userTypeId = req_data['userTypeId']
        data = models.Power.objects.filter(menuId=menuId, userTypeId=userTypeId)
        if len(data) > 0:
            obj = models.Power.objects.get(menuId=menuId, userTypeId=userTypeId)
            obj.menuId = menuId
            obj.menuName = menuName
            obj.power = power
            obj.save()
            return resBack(HttpResponse, False, '操作成功!', '')
        




