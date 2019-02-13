from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import admin.model.article as models #创建数据库表的模块
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
            data = valuesFun(models.Article.objects.filter(typeId=typeId)[x:y].values())
        except:
           data = valuesFun(models.Article.objects.all()[x:y].values())
        return resBack(HttpResponse, False, '查询成功!', data)
# 新增
def Add(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        title = req_data['title']
        content = req_data['content']
        time = req_data['time']
        typeId = req_data['typeId']
        isPublish = req_data['isPublish']
        models.Article.objects.create(title=title, content=content, time=time, typeId=typeId, isPublish=isPublish)
        return resBack(HttpResponse, False, '添加成功!', '')

# 编辑
def Edit(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        id = req_data['id']
        title = req_data['title']
        content = req_data['content']
        typeId = req_data['typeId']
        isPublish = req_data['isPublish']
        data = models.Article.objects.get(pk=id)
        data.title = title
        data.content = content
        data.typeId = typeId
        data.isPublish = isPublish
        data.save()
        return resBack(HttpResponse, False, '编辑成功!', '')
# 查看详情
def Detail(req):
    if req.method == "GET":
        id = req.GET.get('id')
        data = valuesFun(models.Article.objects.filter(pk=id).values())[0]
        return HttpResponse(json.dumps(data),'utf-8',200)

def Del(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.Article.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '删除成功!', '')
