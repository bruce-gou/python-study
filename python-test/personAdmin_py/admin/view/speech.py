from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import admin.model.speech as models #创建数据库表的模块
from common.base import resBack, valuesFun

# 查询所有列表
def List(req):
    if req.method == "GET":
        req_data = req.GET
        pageSize = req_data['pageSize']
        pageNumber = req_data['pageNumber']
        x,y = computPage(pageSize, pageNumber)
        data = valuesFun(models.Speech.objects.all()[x:y].values())
        return resBack(HttpResponse, False, '查询成功!', data)
# 审核
def Assess(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        id = req_data['id']
        isCheck = req_data['isCheck']
        obj = models.Speech.objects.get(id=id)
        obj.isCheck = isCheck
        obj.save()
        return resBack(HttpResponse, False, '操作成功!', '')
# 删除
def Del(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.Speech.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '操作成功!', '')