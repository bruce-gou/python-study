from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import admin.model.menu as models #创建数据库表的模块
import admin.model.power as powerModels #创建数据库表的模块
from common.base import resBack, valuesFun, getToken, getTree

# 查询菜单
def getMenu(req):
    token = getToken(req)
    if req.method == "GET":
        #  获取可用的菜单数据
        menu = valuesFun(models.Menu.objects.filter(isEnable=1).values())
        data = []
        if token['role'] == 1: #超级管理员展示全部，不需要根据权限选择
            data = getTree(menu, 0, 'parentId', 'children')
        else:# 根据权限获取菜单
            power = valuesFun(powerModels.Power.objects.filter(userTypeId=token['role']).values())
            data2 = []
            for x in menu:
                for y in power:
                    if y['menuId'] == x['id']:
                        data2.append(x)
            data = getTree(data2, 0, 'parentId', 'children')
        return HttpResponse(json.dumps(data),'utf-8',200)

# 菜单列表
def List(req):
    if req.method == "GET":
        menu = valuesFun(models.Menu.objects.all().values())
        for i in menu:
            allPower = i.get('allPower')
            if len(allPower) > 0:
                allPower = allPower.split(',')
            else:
                allPower = []
            i['allPower'] = allPower
        data = getTree(menu, 0, 'parentId', 'children')
        return HttpResponse(json.dumps(data),'utf-8',200)

# 新增菜单
def Add(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        allPower = req_data['allPower']
        allPower = ','.join(allPower)
        icon = req_data['icon']
        isEnable = req_data['isEnable']
        name = req_data['name']
        orderNumber = req_data['orderNumber']
        parentId = req_data['parentId']
        path = req_data['path']
        models.Menu.objects.create(name=name, icon=icon, path=path, orderNumber=orderNumber, isEnable=isEnable, parentId=parentId, allPower=allPower)
        return resBack(HttpResponse, False, '添加成功!', '')

# 禁用
def Enable(req):
    if req.method == "GET":
        id = req.GET.get('id')
        isEnable = req.GET.get('isEnable')
        obj = models.Menu.objects.get(id=id)
        obj.isEnable = isEnable
        obj.save()
        return resBack(HttpResponse, False, '操作成功!', '')
# 编辑
def Edit(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        id = req_data['id']
        allPower = req_data['allPower']
        name = req_data['name']
        orderNumber = req_data['orderNumber']
        path = req_data['path']
        icon = req_data['icon']
        obj = models.Menu.objects.get(id=id)
        obj.allPower = ','.join(allPower)
        obj.name = name
        obj.orderNumber = orderNumber
        obj.path = path
        obj.icon = icon
        obj.save()
        return resBack(HttpResponse, False, '操作成功!', '')
# 删除
def Del(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.Menu.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '删除成功!', '')