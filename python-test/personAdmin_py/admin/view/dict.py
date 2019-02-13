from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import admin.model.dict as models #创建数据库表的模块
from common.base import resBack, valuesFun

# 查询所有字典
def AllDict(req):
    if req.method == "GET":
        dictType = valuesFun(models.DictType.objects.all().values()) # 字典类型
        dict = valuesFun(models.Dict.objects.all().values()) # 字典
        # 数据处理
        def dataProcess(data, data1):
            list = []
            for x in data:
                obj = {}
                obj['name'] = x['name']
                obj['data'] = []
                for y in data1:
                    if x['id'] == y['typeId']:
                        obj['data'].append(y)
                list.append(obj)
            return list
        arr = dataProcess(dictType, dict)
        return HttpResponse(json.dumps(arr),'utf-8',200)
# 字典类型列表查询
def TypeList(req):
    if req.method == 'GET':
        data = valuesFun(models.DictType.objects.all().values())
        return HttpResponse(json.dumps(data),'utf-8',200)
# 字典类型新增
def AddType(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        name = req_data['name']
        data = models.DictType.objects.filter(name=name)
        if len(data) == 0:
            models.DictType.objects.create(name=name)
            return resBack(HttpResponse, False, '添加成功!', '')
        else:
            return resBack(HttpResponse, True, '数据已存在!', '')
# 删除字典类型
def DelType(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.DictType.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '删除成功!', '')

# 根据类型查询字典列表
def List(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        data = valuesFun(models.Dict.objects.filter(typeId=id).values())
        return HttpResponse(json.dumps(data),'utf-8',200)

# 新增字典
def Add(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        code = req_data["code"]
        name = req_data["name"]
        typeId = req_data["typeId"]
        models.Dict.objects.create(code=code, name=name, typeId=typeId)
        return resBack(HttpResponse, False, '添加成功!', '')
# 字典编辑
def Edit(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        code = req_data["code"]
        name = req_data["name"]
        id = req_data["id"]
        obj = models.Dict.objects.get(pk=id)
        obj.code = code
        obj.name = name
        obj.save()
        return resBack(HttpResponse, False, '修改成功!', '')
# 字典删除
def Del(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.Dict.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '删除成功!', '')





