from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import login.models as models #创建数据库表的模块
from common.base import resBack, valuesFun, computPage


# 用户列表
def List(req):
    if req.method == "GET":
        req_data = req.GET
        pageSize = req_data['pageSize']
        pageNumber = req_data['pageNumber']
        x,y = computPage(pageSize, pageNumber)
        data = []
        try:
            name = req_data['name']
            data = valuesFun(models.Users.objects.filter(name=name)[x:y].values())
        except:
           data = valuesFun(models.Users.objects.all()[x:y].values())
        return resBack(HttpResponse, False, '查询成功!', data)
# 新增用户
def Add(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        user = req_data['user']
        role = req_data['role']
        if int(role) == 1:
            return resBack(HttpResponse, True, '超级管理员已经存在!', '')
        data = models.Users.objects.filter(user=user)
        if len(data) == 0:
            name = req_data['name']
            pwd = req_data['pwd']
            roleName = req_data['roleName']
            tel = req_data['tel']
            mailbox = req_data['mailbox']
            isEnable = req_data['isEnable']
            models.Users.objects.create(name=name, user=user, pwd=pwd, role=role, roleName=roleName, tel=tel, mailbox=mailbox, isEnable=isEnable)
            return resBack(HttpResponse, False, '添加成功!', '')
        else:
            return resBack(HttpResponse, True, '账号已经存在!', '')

# 重置密码
def EditPwd(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        id = req_data['id']
        pwd = req_data['pwd']
        obj = models.Users.objects.get(pk=id)
        obj.pwd = pwd
        obj.save()
        return resBack(HttpResponse, False, '操作成功!', '')

# 编辑
def Edit(req):
    if req.method == "POST":
        req_data = json.loads(req.body)
        isEnable = req_data['isEnable']
        role = req_data['role']
        roleName = req_data['roleName']
        id = req_data['id']
        if int(role) == 1:
            return resBack(HttpResponse, True, '超级管理员已经存在!', '')
        obj = models.Users.objects.get(pk=id)
        obj.isEnable = isEnable
        obj.role = role
        obj.roleName = roleName
        obj.save()
        return resBack(HttpResponse, False, '修改成功!', '')

# 删除
def Del(req):
    if req.method == "GET":
        id = req.GET.get('id')
        models.Users.objects.filter(id=id).delete()
        return resBack(HttpResponse, False, '删除成功!', '')


