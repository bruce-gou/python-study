from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import admin.model.resources as models #创建数据库表的模块
from common.base import resBack, valuesFun, computPage

# 查询所有列表
def List(req):
    if req.method == "GET":
        req_data = req.GET
        pageSize = req_data['pageSize']
        pageNumber = req_data['pageNumber']
        x,y = computPage(pageSize, pageNumber)
        data = []
        try:
            typeId = req_data['typeId']
            data = valuesFun(models.Resources.objects.filter(typeId=typeId)[x:y].values())
        except:
           data = valuesFun(models.Resources.objects.all()[x:y].values())
        return resBack(HttpResponse, False, '查询成功!', data)
# 新增
def Add(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        name = req_data['name']
        url = req_data['url']
        typeId = req_data['typeId']
        models.Resources.objects.create(typeId=typeId, name=name, url=url)
        return resBack(HttpResponse, False, '添加成功!', '')

# 编辑
def Edit(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        id = req_data['id']
        name = req_data['name']
        url = req_data['url']
        typeId = req_data['typeId']
        obj = models.Resources.objects.get(pk=id)
        obj.name = name
        obj.url = url
        obj.typeId = typeId
        obj.save()
        return resBack(HttpResponse, False, '编辑成功!', '')

# 删除
def Del(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.Resources.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '删除成功!', '')
